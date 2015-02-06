from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from interfaithclimate.theme.content.frontpage_image import IFrontpageImage

#grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):
    
    title = schema.TextLine(
            title = u"Any dummy title"    
        )
    
    

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    def __init__(self,path=None):
        self.path = path
        
    title = u"Slider portlet"
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('image_slider.pt')
    
    
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
    def contents(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog.unrestrictedSearchResults(object_provides = IFrontpageImage.__identifier__)
        results = []
        for brain in brains:
            obj = brain._unrestrictedGetObject()
            subData = {'txt_img':'', 'bg_img':'', 'link':''}
            if obj.text_image:
                subData['txt_img'] = brain.getPath()+'/@@images/text_image'
            if obj.bg_image:
		subData['bg_img'] = brain.getPath()+'/@@images/bg_image'
	    subData['link'] = obj.img_link
	    results.append(subData)
	return results

        
    

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Image Slider Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment
    

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Image Slider Portlet"
    description = ''
