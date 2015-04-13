#!/usr/bin/env python


class Element(object):

    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        self.el = [str(content)] if content else []

    def append(self, string):
        self.el.append(string)

    def render(self, file_out, ind=""):

        file_out.write(ind + "<" + self.tag + ">\n")

        for i in self.el:
            try:
                i.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(self.indent + ind + unicode(i) + "\n")

        file_out.write(ind + "</" + self.tag + ">\n")

class Html(Element):
    header = u"<!DOCTYPE html>\n"
    tag = u"html"

class Body(Element):
    tag = u"body"

class P(Element):
    tag = u"p"
