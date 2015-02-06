from five import grok
from plone.directives import dexterity, form
from interfaithclimate.theme.content.frontpage_image import IFrontpageImage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IFrontpageImage)
    grok.require('zope2.View')
    grok.template('frontpage_image_view')
    grok.name('view')

