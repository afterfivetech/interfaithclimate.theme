from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder

grok.templatedir('templates')

class events_listing_customview(grok.View):
    grok.context(IATFolder)
    grok.require('zope2.View')
    
    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def contents(self):
        context = self.context
        brains = self.catalog.unrestrictedSearchResults(path={'query':'/'.join(context.getPhysicalPath()), 'depth':1, 'sort_order':'reverse', 'sort_on':'created'})
        results = []
        for brain in brains:
            data = {}
            data['item_url'] = brain.getPath()
            data['item_creator'] = brain.Creator
            if hasattr(brain._unrestrictedGetObject(),'start'):
                data['item_start'] = brain._unrestrictedGetObject().start()
            elif hasattr(brain._unrestrictedGetObject(),'StartDate'):
                data['item_start'] = brain._unrestrictedGetObject().StartDate()
            else:
                data['item_start'] = None
            data['item_title_or_id'] = brain.pretty_title_or_id()
            data['item_type'] = brain.portal_type
            data['hasContentLeadImage'] = brain.hasContentLeadImage
            data['lead_image'] = brain.getPath()+'/leadImage_preview'
            results.append(data)
        if results:
            results.sort(key=lambda x:x['item_start'], reverse=True)
        return results[:10]
    

    