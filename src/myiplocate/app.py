import grok

from myiplocate import resource

class Myiplocate(grok.Application, grok.Container):
    pass

class Index(grok.View):
    def update(self):
        resource.style.need()
