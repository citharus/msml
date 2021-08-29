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


class Element:
    def __init__(self, pattern: str, replacement: str) -> None:
        self.pattern: str = pattern
        self.replacement: str = replacement
        self.content: Optional[str] = None

    def match(self, string: str) -> bool:
        if match := re.match(self.pattern, string):
            self.content: str = match.groups()[0]
            return True
        return False

    def replace(self) -> str:
        return self.replacement.replace('content', self.content)


class Quote(Element):
    def __init__(self):
        super(Quote, self).__init__(
            r'(?:#q\s*)([\w.]+(?: +[\w.]+)*)',
            '<blockquote>\n\t{content}\n</blockquote>\n',
        )


class Highlight(Element):
    def __init__(self):
        super(Highlight, self).__init__(
            '(?:#hl\s*)([\w.]+(?: +[\w.]+)*)(?:\s*hl#)',
            '<hl>{content}</hl>',
        )
