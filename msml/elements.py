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

__all__: list[str] = ['Quote', 'Highlight', 'Math', 'Image']


class Element:
    pattern: str = None
    replacement: str = None

    @classmethod
    def __call__(cls, string: str) -> Optional[str]:
        if match := re.match(cls.pattern, string):
            return cls.replacement.replace('{content}', match.groups()[0])
        return None


class Quote(Element):
    pattern = r'(?:#q\s*)([\w.]+(?: +[\w.]+)*)'
    replacement = '<blockquote>{content}</blockquote>\n'


class Highlight(Element):
    pattern = '(?:#hl\s*)([\w.]+(?: +[\w.]+)*)(?:\s*hl#)'
    replacement = '<hl>{content}</hl>'


class Math(Element):
    pattern = '(?:#m\s*)([ \w=/.()]+)'
    replacement = '<blockquote class="math">{content}</blockquote>\n'


class Image(Element):
    pattern = '(?:#img\s*)([/\w]+\.(?:png|jpg|gif))'
    replacement = '<img src="{content}">\n'
