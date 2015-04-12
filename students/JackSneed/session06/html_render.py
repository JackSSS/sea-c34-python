#!/usr/bin/env python


class Element(object):

    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else {}

    def append(self, string):
        """Append string to content."""
        self.content.append(string)

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        file_out.write(self.output(ind))

class Html(Element):
    """HTML tag."""

    tag = u"html"

class Body(Element):
    """Body tag."""

    tag = u"body"
