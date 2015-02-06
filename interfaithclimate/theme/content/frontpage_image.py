from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
#from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from interfaithclimate.theme import MessageFactory as _


# Interface class; used to define content-type schema.

class IFrontpageImage(form.Schema, IImageScaleTraversable):
    """
    Source of Frontpage Images
    """
    text_image = NamedBlobFile(
            title=_(u"Text Image Attachment"),
            required=False,
        )

    bg_image = NamedBlobFile(
            title=_(u"Background Image Attachment"),
            required=False,
        )

    img_link = schema.TextLine(
            title=_(u"Image Link"),
            required=False,
        )
    pass

alsoProvides(IFrontpageImage, IFormFieldProvider)
