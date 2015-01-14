from collective.grok import gs
from interfaithclimate.theme import MessageFactory as _

@gs.importstep(
    name=u'interfaithclimate.theme', 
    title=_('interfaithclimate.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('interfaithclimate.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
