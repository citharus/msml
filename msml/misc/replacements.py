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

PAGE_HEADING: str = '<h1>{content}</h1>\n'
SECTION_HEADING: str = '<h2>{content}</h2>\n'

SECTION: str = '<section>\n\t{content}\n</section>\n'

QUOTE: str = '<blockquote>\n\t{content}\n</blockquote>\n'
HIGHLIGHT: str = '<hl>{content}</hl>'
MATH: str = '<blockquote class="math">\n\t{content}\n</blockquote>\n'
IMAGE: str = '<img src="{content}">\n'

PAGE: str = '''<!DOCTYPE html>
<html>
<head>
    <title>{page_heading}</title>
    <script>
    MathJax = { loader: { load: [ "input/asciimath", "output/svg" ] } };
    </script>
    <script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3.1/es5/startup.js">
    </script>
</head>
<body>
    {page_heading}
    
    {sections}
</body>
</html>'''
