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

from pathlib import Path
from typing import Optional, Union, Tuple

from msml.elements import *

__all__: list[str] = ['Parser']


class Parser:
    def __init__(self, file_path: Union[Path, str]) -> None:
        self.file_path: str = file_path

    def __file_lines(self) -> list[str]:
        with open(self.file_path, 'r') as file:
            return file.readlines()

    def get_info(self) -> Tuple[str, str]:
        page_heading: Optional[str] = None
        page_description: Optional[str] = None

        for line in self.__file_lines():
            if page_heading and page_description:
                break
            elif heading := PageHeading().match(line):
                page_heading: str = heading
            elif description := PageDescription().match(line):
                page_description: str = description

        return page_heading, page_description

    def get_sections(self) -> list[str]:
        sections: list[str] = []

        for line in self.__file_lines():
            if section := SectionHeading().match(line):
                sections.append(section)
            elif quote := Quote().match(line):
                sections[-1] += quote
            elif highlight := Highlight().match(line):
                sections[-1] += highlight
            elif math := Math().match(line):
                sections[-1] += math
            elif image := Image().match(line):
                sections[-1] += image
            elif linebreak := LineBreak().match(line):
                if sections:
                    sections[-1] += linebreak
            else:
                if sections:
                    sections[-1] += line

        for index, section in enumerate(sections):
            sections[index] = f'<section>\n{section}</section>'

        return sections
