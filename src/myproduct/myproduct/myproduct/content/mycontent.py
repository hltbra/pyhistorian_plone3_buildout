"""Definition of the mycontent content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from myproduct.myproduct.interfaces import Imycontent
from myproduct.myproduct.config import PROJECTNAME

mycontentSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

mycontentSchema['title'].storage = atapi.AnnotationStorage()
mycontentSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(mycontentSchema, moveDiscussion=False)


class mycontent(base.ATCTContent):
    """Description of the Example Type"""
    implements(Imycontent)

    meta_type = "mycontent"
    schema = mycontentSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(mycontent, PROJECTNAME)
