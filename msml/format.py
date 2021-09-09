#  MIT License
#
#  Copyright (c) 2021-present citharus
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

try:
    from bs4 import BeautifulSoup

    bs4: bool = True
except ModuleNotFoundError:
    bs4: bool = False

import pathlib
from os import mkdir

import pdfkit

import msml.parse as parse
import msml.paths as paths

__all__: list[str] = ['Formatter']


class Formatter:
    def __init__(
            self,
            file: str,
            out_dir: str = 'out',
            *,
            template: str = 'default',
            stylesheet: str = 'default',
    ) -> None:
        self.file: pathlib.Path = pathlib.Path(file)
        self.out_dir: pathlib.Path = pathlib.Path(out_dir)
        self.template: pathlib.Path = paths.TEMPLATES.joinpath(
            f'{template}.html',
        )
        self.stylesheet: pathlib.Path = paths.STYLESHEETS.joinpath(
            f'{stylesheet}.css',
        )

    def make_html(self) -> str:
        parser: parse.Parser = parse.Parser(self.file)
        page_heading, page_description = parser.get_info()
        sections: list[str] = parser.get_sections()

        with self.template.open() as template:
            html: str = template.read()
            html = html.replace('{page_heading}', page_heading)
            html = html.replace('{sections}', '\n'.join(sections))

            with self.stylesheet.open() as stylesheet:
                html = html.replace('{stylesheet}', stylesheet.read())

        if bs4:
            return BeautifulSoup(html, features='html.parser').prettify()
        return html

    def make_pdf(self) -> bytes:
        return pdfkit.from_string(
            input=self.make_html(),
            output_path=False,
            options={
                'enable-local-file-access': False,
                'encoding': 'utf-8',
            },
            css=self.stylesheet,
        )

    def write(self, _type: str) -> None:
        if not self.out_dir.exists():
            mkdir(str(self.out_dir))

        if _type not in ['pdf', 'html']:
            return None

        with open(f'{self.out_dir}/{self.file.name}.{_type}', 'w') as outfile:
            if _type is 'pdf':
                outfile.write(self.make_pdf())
            outfile.write(self.make_html())
