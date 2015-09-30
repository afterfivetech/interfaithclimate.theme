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


#grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):
    
    portlet_header = schema.TextLine(
            title = u"Portlet Header",
            default = u"TWITTER FEED",
            required = False
        )

    twitter_username = schema.TextLine(
            title = u"Twitter Username",
            default = u"isclimatechange"
        )

    twitter_widgetId = schema.TextLine(
            title = u"Twitter Widget ID",
            default = u"565570873433006080"
        )

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    
    def __init__(self,portlet_header=None, twitter_username= None, twitter_widgetId=None):
        self.portlet_header = portlet_header
        self.twitter_username = twitter_username
        self.twitter_widgetId = twitter_widgetId
       
    @property
    def title(self):
        return self.portlet_header
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('twitterportlet.pt')
    
    
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
        
    def contents(self):
        return self.data

        
    

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Twitter Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment
    

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Twitter Portlet"
    description = ''
