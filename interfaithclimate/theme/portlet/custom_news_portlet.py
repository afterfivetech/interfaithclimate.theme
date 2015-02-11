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
from plone.app.portlets.cache import render_cachekey
from plone.app.portlets import PloneMessageFactory as _
from plone.memoize import ram
from plone.app.portlets.portlets import base
from Acquisition import aq_inner
from plone.memoize.compress import xhtml_compress
from plone.app.layout.navigation.root import getNavigationRootObject

#grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):
    
    count = schema.Int(title=_(u'Number of items to display'),
                       description=_(u'How many items to list.'),
                       required=True,
                       default=3)

    state = schema.Tuple(title=_(u"Workflow state"),
                         description=_(u"Items in which workflow state to show."),
                         default=('published', ),
                         required=True,
                         value_type=schema.Choice(
                             vocabulary="plone.app.vocabularies.WorkflowStates")
                         )
    
    

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    def __init__(self, count=5, state=('published', )):
        self.count = count
        self.state = state
        
    title = u"Custom News Portlet"
    

class Renderer(base.Renderer):
    _render = ViewPageTemplateFile('custom_news_portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    #@ram.cache(render_cachekey)
    def render(self):
        return xhtml_compress(self._render())

    @property
    def available(self):
        return self.data.count > 0 and len(self._data())

    def published_news_items(self):
        return self._data()

    def all_news_link(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request),
            name='plone_portal_state')
        portal = portal_state.portal()
        if 'news' in getNavigationRootObject(context, portal).objectIds():
            return '%s/news' % portal_state.navigation_root_url()
        return None

    #@memoize
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name='plone_portal_state')
        
        path = portal_state.navigation_root_path()
        limit = self.data.count
        state = self.data.state
        return catalog(portal_type='News Item',
                       review_state=state,
                       path=path,
                       sort_on='Date',
                       sort_order='reverse',
                       sort_limit=limit)[:limit]


    
    
    def newsDescription(self, data=None):
        if data:
            if len(data) > 100:
                return data[:101]+' ...'
        return data
        		


        
    

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Custom News Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment
        #return Assignment(count=data.get('count', 5), state=data.get('state', ('published', )))
    

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Custom News Portlet"
    description = ''
