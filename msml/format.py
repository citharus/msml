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

from msml.parse import Parser

__all__: list[str] = ['Formatter']


class Formatter:
    def __init__(self, file: str, out_dir_name: str = 'out') -> None:
        self.file: pathlib.Path = pathlib.Path(file)
        self.out_dir_name: pathlib.Path = pathlib.Path(out_dir_name)

    def format(self) -> str:
        parser: Parser = Parser(self.file)
        page_heading, page_description = parser.get_info()
        sections: list[str] = parser.get_sections()

        with open('assets/template.html', 'r') as file:
            html: str = file.read()
            html = html.replace('{page_heading}', page_heading)
            html = html.replace('{sections}', '\n'.join(sections))

        if bs4:
            return BeautifulSoup(html, features='html.parser').prettify()
        return html
