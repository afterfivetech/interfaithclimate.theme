from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder

grok.templatedir('templates')

class news_listing_customview(grok.View):
    grok.context(IATFolder)
    grok.require('zope2.View')
    
    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def contents(self):
        context = self.context
        brains = self.catalog.unrestrictedSearchResults(path={'query':'/'.join(context.getPhysicalPath()), 'depth':1, 'sort_on':'created', 'sort_order':'reverse'}, portal_type='News Item')
        results = []
        for brain in brains:
            data = {}
            data['item_url'] = brain.getPath()
            data['item_creator'] = brain.Creator
            data['item_created'] = brain.created
            data['item_modified'] = brain.modified
            data['item_title_or_id'] = brain.pretty_title_or_id()
            data['item_type'] = brain.portal_type
            data['hasImage'] = brain._unrestrictedGetObject().getImage()
            data['image'] = brain.getPath()+'/image_large'
            data['item_description'] = brain.Description
            results.append(data)
        if results:
            results.sort(key=lambda x:x['item_created'])
        
        return results
