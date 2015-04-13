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

    def render(self, file_out, ind=u""):

        file_out.write(ind + "<" + self.tag + self.attr + ">\n")
        for i in self.el:
            try:
                i.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(self.indent + ind + unicode(i) + "\n")

        file_out.write(ind + "</" + self.tag + ">\n")

class OneLineTag(Element):

    def render(self, file_out, ind=u""):

        file_out.write(ind + "<" + self.tag + ">")
        for i in self.el:
            try:
                i.render(file_out, ind=u"")
            except AttributeError:
                file_out.write(unicode(i))

        file_out.write("</" + self.tag + ">\n")

class Html(Element):
    header = u"<!DOCTYPE html>\n"
    tag = u"html"

    def render(self, file_out, indent=u""):

        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, indent)

class Head(Element):
    tag = u"head"

class Meta(SelfClosingTag):
    tag = u"meta"

class Body(Element):
    tag = u"body"

class Title(OneLineTag):
    tag = u"title"

class P(Element):
    tag = u"p"

class SelfClosingTag(Element):
    def render(self, file_out, ind=u""):
        file_out.write(ind + "<" + self.tag + self.attr + "> \n")

class Hr(SelfClosingTag):
    tag = u"hr"


class Br(SelfClosingTag):
    tag = u"br"

class A(OneLineTag):
    tag = u'a'

    def __init__(self, link, content=None):
        self.link = link
        Element.__init__(self, content, href=link)

class Ul(Element):
    tag = u"ul"


class Li(Element):
    tag = u"li"


class H(OneLineTag):
    tag = u"h"

    def __init__(self, level, content=None):
        self.tag = "%s%i" % (H.tag, level)
        Element.__init__(self, content)
