#!/usr/bin/env python


class Element(object):

    tag = u"html"
    indent = u"    "

    def __init__(self, content=None, **kwargs):
        self.el = [str(content)] if content else []
        self.attributes = kwargs
        self.attr = u""
        for k, v in self.attributes.items():
            self.attr += u" %s = %s" % (k, v)

    def append(self, string):
        self.el.append(string)

    def render(self, file_out, ind=""):

        file_out.write(ind + "<" + self.tag + self.attr + ">\n")
        for i in self.el:
            try:
                i.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(self.indent + ind + unicode(i) + "\n")

        file_out.write(ind + "</" + self.tag + ">\n")

class OneLineTag(Element):

    def render(self, file_out, ind=""):

        file_out.write(ind + "<" + self.tag + ">")
        for i in self.el:
            try:
                i.render(file_out, ind="")
            except AttributeError:
                file_out.write(unicode(i))

        file_out.write("</" + self.tag + ">\n")

class Html(Element):
    header = u"<!DOCTYPE html>\n"
    tag = u"html"

class Head(Element):
    tag = u"head"

class Body(Element):
    tag = u"body"

class Title(OneLineTag):
    tag = u"title"

class P(Element):
    tag = u"p"

