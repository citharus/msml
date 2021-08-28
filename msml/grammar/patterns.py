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

import re

__all__: list[str] = [
    'PAGE_HEADING',
    'SECTION_HEADING',
    'HEADING_3',
    'DESCRIPTION',
    'QUOTE',
    'HIGHLIGHT',
    'MATH',
    'IMAGE',
]

_text: str = r'(?P<text>[\w\.]+(?: +[\w\.]+)*)'

PAGE_HEADING: re.Pattern = re.compile(
    rf'(?:#hp\s*){_text}',
    re.IGNORECASE,
)
SECTION_HEADING: re.Pattern = re.compile(
    rf'(?:#hs\s*){_text}',
    re.IGNORECASE,
)
SUB_SECTION_HEADING: re.Pattern = re.compile(
    rf'(?:#hss\s*){_text}',
    re.IGNORECASE,
)

DESCRIPTION: re.Pattern = re.compile(
    rf'(?:#d\s*){_text}',
    re.IGNORECASE,
)

QUOTE: re.Pattern = re.compile(
    rf'(?:#q\s*){_text}',
    re.IGNORECASE,
)

HIGHLIGHT: re.Pattern = re.compile(
    rf'(?:#hl\s*){_text}(?:\s*hl#)',
    re.IGNORECASE,
)

MATH: re.Pattern = re.compile(
    rf'(?:#m\s*)(?P<term>[ \w=/.()]+)',
    re.IGNORECASE,
)

IMAGE: re.Pattern = re.compile(
    r'(?:#img\s*)(?P<source>[/\w]+\.(?:png|jpg|gif))(?:\s*)(?P<alt>\w+)',
    re.IGNORECASE,
)
