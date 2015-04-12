#!/usr/bin/env python


class Element(object):

    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""

    def append(self, string):
        self.content += (self.indent + string)

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        output = (self.indent + "<" + self.tag + ">\n"
                     + self.indent + self.content + "\n"
                     + self.indent + "</" + self.tag + ">")
        file_out.write(output)

