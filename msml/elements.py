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
from typing import Optional

__all__: list[str] = [
    'PageHeading',
    'SectionHeading',
    'Quote',
    'Highlight',
    'Math',
    'Image',
    'LineBreak',
]


class Element:
    pattern: Optional[str] = None
    replacement: str = ''

    @classmethod
    def match(cls, string: str) -> Optional[str]:
        if match := re.match(cls.pattern, string):
            return cls.replacement.replace('{content}', match.groups()[0])
        return None


class PageHeading(Element):
    pattern: str = r'(?:#hp\s*)([\w.]+(?: +[\w.]+)*)'
    replacement: str = '<h1>{content}</h1>\n'


class Description(Element):
    pattern: str = r'(?:#d\s*)([\w.]+(?: +[\w.]+)*)'
    replacement: str = ''


class SectionHeading(Element):
    pattern: str = r'(?:#hs\s*)([\w.]+(?: +[\w.]+)*)'
    replacement: str = '<h2>{content}</h2>\n'


class Quote(Element):
    pattern: str = r'(?:#q\s*)([\w.]+(?: +[\w.]+)*)'
    replacement: str = '<blockquote>{content}</blockquote>\n'


class Highlight(Element):
    pattern: str = r'(?:#hl\s*)([\w.]+(?: +[\w.]+)*)(?:\s*hl#)'
    replacement: str = '<hl>{content}</hl>'


class Math(Element):
    pattern: str = r'(?:#m\s*)([ \w=/.()]+)'
    replacement: str = '<blockquote class="math">`{content}`</blockquote>\n'


class Image(Element):
    pattern: str = r'(?:#img\s*)([/\w]+\.(?:png|jpg|gif))'
    replacement: str = '<img src="{content}">\n'


class LineBreak(Element):
    pattern: str = r'(\n)'
    replacement: str = '<br>\n'
