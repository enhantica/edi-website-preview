#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
"""Build the public-website design alternatives without the native edi toolchain."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parent
CONCEPTS = {
    'surfaces': (
        'Choose your interface',
        'Application, Python and Command Line have their own top-level sections.',
    ),
    'workflows': (
        'Follow your workflow',
        'Shared guides explain the science; interface tabs show how to do it.',
    ),
}


def _write_reference(built: Path, base_url: str) -> None:
    """Publish the same authored text for retrieval, with canonical working links."""
    docs = ROOT / 'surfaces' / 'docs'
    index = [
        '# EasyDiffraction',
        '',
        '> Scientific explanations and interface instructions for the new EasyDiffraction.',
        '',
        'Identify experiment type, radiation, model and units before selecting an equation.',
        'Cite its exact section. Stored-only fields are not active calculation terms.',
        'The model catalogue records the inspected source snapshot. Interface availability',
        'comes from Features and roadmap; planned or proposed work is not available functionality.',
        'This export supplies reference content; it does not implement a chat integration.',
        '',
        f'- [Model and parameter catalogue]({base_url}physics/catalogue.json)',
        '',
        '## Documentation in Markdown',
        '',
    ]
    for source in sorted(docs.rglob('*.md')):
        relative = source.relative_to(docs)
        text = source.read_text(encoding='utf-8')
        text = re.sub(r'\A---\n.*?\n---\n', '', text, count=1, flags=re.DOTALL).lstrip()
        route = relative.parent if relative.name == 'index.md' else relative.with_suffix('')
        canonical = base_url + (route.as_posix().strip('.') + '/').lstrip('/')

        def link(match: re.Match[str], canonical: str = canonical, source: Path = source) -> str:
            value = match.group(1)
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or value.startswith('/'):
                return match.group(0)
            if not parsed.path:
                return '](' + canonical + value + ')'
            target = (source.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(docs):
                raise SystemExit(f'Reference link escapes docs: {source}: {value}')
            target_relative = target.relative_to(docs)
            if target.suffix == '.md':
                target_route = (
                    target_relative.parent
                    if target.name == 'index.md'
                    else target_relative.with_suffix('')
                )
                url = base_url + (target_route.as_posix().strip('.') + '/').lstrip('/')
            else:
                url = base_url + target_relative.as_posix()
            if parsed.fragment:
                url += '#' + parsed.fragment
            return '](' + url + ')'

        # Leave code examples unchanged: paths in code are instructions, not document links.
        blocks = re.split(r'(^```[^\n]*\n.*?^```[^\n]*$)', text, flags=re.MULTILINE | re.DOTALL)
        text = ''.join(
            block if number % 2 else re.sub(r'\]\(([^\s)]+)\)', link, block)
            for number, block in enumerate(blocks)
        )
        destination = built / 'reference' / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(f'Canonical page: {canonical}\n\n{text}', encoding='utf-8')
        title = re.search(r'^# (.+)$', text, flags=re.MULTILINE)
        index.append(
            f'- [{title[1] if title else relative}]({base_url}reference/{relative.as_posix()})'
        )
    (built / 'llms.txt').write_text('\n'.join(index) + '\n', encoding='utf-8')


def _check_catalogue(built: Path) -> None:
    """A model/parameter lookup must resolve to an actual explanatory heading."""
    physics = built / 'physics'
    catalogue = json.loads((physics / 'catalogue.json').read_text(encoding='utf-8'))
    seen = set()

    class Headings(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.ids: set[str] = set()

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag in {'h1', 'h2', 'h3', 'h4'}:
                self.ids.update(value for key, value in attrs if key == 'id' and value)

    for group in ('models', 'parameters'):
        for entry in catalogue[group]:
            identity = (group, entry['category'], entry['id'])
            if identity in seen:
                raise SystemExit(f'Duplicate catalogue entry: {identity}')
            seen.add(identity)
            for field in ('explanation_url', 'parameter_url'):
                if field not in entry:
                    continue
                url = urlsplit(entry[field])
                target = (physics / url.path / 'index.html').resolve()
                if url.scheme or url.netloc or not target.is_relative_to(physics):
                    raise SystemExit(f'Invalid catalogue URL: {entry[field]}')
                parser = Headings()
                parser.feed(target.read_text(encoding='utf-8'))
                if not url.fragment or url.fragment not in parser.ids:
                    raise SystemExit(f'Catalogue heading missing: {entry[field]}')
    print('Scientific catalogue explanation/parameter headings: PASS', flush=True)


def _write_redirects(root: Path, base_url: str) -> None:
    """Keep links to relocated shared guides valid without a theme plugin."""
    redirects = json.loads((ROOT / 'redirects.json').read_text(encoding='utf-8'))
    for old, new in redirects.items():
        for route in (old, new):
            if not isinstance(route, str) or not re.fullmatch(r'(?:[a-z0-9-]+/)+', route):
                raise SystemExit(f'Invalid redirect route: {route!r}')
        target = root / new / 'index.html'
        destination = root / old / 'index.html'
        if not target.is_file() or (
            destination.exists()
            and '<title>Page moved - EasyDiffraction</title>' not in destination.read_text()
        ):
            raise SystemExit(f'Redirect must point to a page and not replace one: {old} -> {new}')
        relative = escape(posixpath.relpath(new, old) + '/', quote=True)
        canonical = escape(base_url.rstrip('/') + '/' + new, quote=True)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta http-equiv="refresh" content="0; url={relative}">'
            f'<link rel="canonical" href="{canonical}">'
            '<title>Page moved - EasyDiffraction</title></head><body>'
            f'<a href="{relative}">Continue to the User guide</a></body></html>\n',
            encoding='utf-8',
        )


def _check_links(root: Path, base_url: str | None) -> None:
    prefix = urlsplit(base_url).path.rstrip('/') if base_url else ''
    errors = []

    class Links(HTMLParser):
        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag not in {'a', 'img', 'image', 'script', 'link'}:
                return
            for key, value in attrs:
                if key not in {'href', 'src'} or not value:
                    continue
                parsed = urlsplit(value)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                path = unquote(parsed.path)
                if path.startswith('/'):
                    if prefix and path.startswith(prefix + '/'):
                        path = path[len(prefix) :]
                    target = root / path.lstrip('/')
                else:
                    target = self.file.parent / path
                target = target.resolve()
                if target.is_dir():
                    target /= 'index.html'
                if not target.is_relative_to(root) or not target.is_file():
                    errors.append(f'{self.file.relative_to(root)}: {value}')

    for file in root.rglob('*.html'):
        parser = Links()
        parser.file = file
        parser.feed(file.read_text(encoding='utf-8'))
    if errors:
        raise SystemExit('Broken generated links/assets:\n' + '\n'.join(errors[:10]))
    print('Generated internal links and assets: PASS', flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('concept', choices=[*CONCEPTS, 'all'], nargs='?', default='all')
    parser.add_argument('--base-url', help='Public site root, including the repository URL prefix')
    args = parser.parse_args()
    if args.base_url:
        parsed = urlsplit(args.base_url)
        if (
            parsed.scheme not in {'http', 'https'}
            or not parsed.netloc
            or parsed.query
            or parsed.fragment
        ):
            parser.error('--base-url must be an HTTP(S) URL without a query or fragment')
        args.base_url = args.base_url.rstrip('/') + '/'
    config_data = yaml.load((ROOT / 'surfaces/mkdocs.yml').read_text(), Loader=yaml.BaseLoader)
    stages = list(config_data['extra']['workflow_icons'])
    shared = ['Start here', *stages]
    for interface in ('Application', 'Python', 'Command Line'):
        section = next(entry[interface] for entry in config_data['nav'] if interface in entry)
        groups = [next(iter(entry)) for entry in section if isinstance(entry, dict)]
        if groups[: len(shared)] != shared:
            raise SystemExit(f'{interface}: workflow groups must be {shared}')
    print('Shared interface workflow navigation: PASS', flush=True)
    capture = ROOT / 'surfaces/docs/assets/gui/y2o3'
    if (capture / 'manifest.json').exists():
        from checks.gui_capture import validate_bundle

        validate_bundle(capture)
        print('Native GUI capture bundle: PASS', flush=True)
    version = importlib.metadata.version('zensical')
    if version != '0.0.73':
        raise SystemExit(f'Expected Zensical 0.0.73; found {version}. Install requirements.txt.')
    names = list(CONCEPTS) if args.concept == 'all' else [args.concept]
    output = ROOT / '_build'
    if args.concept == 'all':
        if output.exists():
            shutil.rmtree(output)
    for name in names:
        config = ROOT / name / 'mkdocs.yml'
        temporary = None
        original = config.read_text(encoding='utf-8')
        text = original
        if name == 'surfaces':
            assets = ROOT / 'surfaces/docs/assets'
            digest = hashlib.sha256(
                (assets / 'gui-capture.css').read_bytes()
                + (assets / 'gui-capture.js').read_bytes()
            ).hexdigest()[:12]
            text = text.replace('extra:\n', f'extra:\n  gui_assets_version: {digest}\n', 1)
        if args.base_url:
            text, count = re.subn(
                r'^site_url:.*$',
                f'site_url: {args.base_url}' + (f'{name}/' if name != 'surfaces' else ''),
                text,
                flags=re.MULTILINE,
            )
            if count != 1:
                raise SystemExit(f'{name}: expected exactly one site_url setting')
        if text != original:
            with tempfile.NamedTemporaryFile(
                mode='w',
                dir=config.parent,
                prefix='.preview-',
                suffix='.yml',
                encoding='utf-8',
                delete=False,
            ) as stream:
                stream.write(text)
                temporary = Path(stream.name)
            config = temporary
        try:
            subprocess.run(
                [sys.executable, '-m', 'zensical', 'build', '--strict', '-f', str(config)],
                cwd=ROOT / name,
                check=True,
            )
        finally:
            if temporary:
                temporary.unlink(missing_ok=True)
        built = ROOT / name / 'site'
        if not (built / 'index.html').is_file():
            raise SystemExit(f'{name}: the build did not produce its homepage')
        if name == 'surfaces':
            _write_reference(built, args.base_url or 'http://127.0.0.1:8873/')
            _check_catalogue(built)
        assembled = output if name == 'surfaces' else output / name
        if assembled.exists() and name != 'surfaces':
            shutil.rmtree(assembled)
        shutil.copytree(built, assembled, dirs_exist_ok=name == 'surfaces')
        if name == 'surfaces':
            _write_redirects(assembled, args.base_url or 'http://127.0.0.1:8873/')
            # Preserve published prototype links; canonical URLs point to the site root.
            legacy = output / 'surfaces'
            if legacy.exists():
                shutil.rmtree(legacy)
            shutil.copytree(built, legacy)
            _write_redirects(legacy, args.base_url or 'http://127.0.0.1:8873/')
    _check_links(output.resolve(), args.base_url)
    command = f'python -m http.server 8873 --bind 127.0.0.1 --directory {output}'
    print(f'Preview: {command}', flush=True)


if __name__ == '__main__':
    main()
