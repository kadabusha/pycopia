#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

attribSi_expires_2496959613638388889 = pycopia.XML.POM.XMLAttribute(u'si-expires', 1, 12, None)


attribCreated_4009362612254311225 = pycopia.XML.POM.XMLAttribute(u'created', 1, 12, None)


attribClass_2331018730345177744 = pycopia.XML.POM.XMLAttribute(u'class', 7, 11, None)


attribHref_2430637454403731329 = pycopia.XML.POM.XMLAttribute(u'href', 1, 12, None)


attribSi_id_809765079235731441 = pycopia.XML.POM.XMLAttribute(u'si-id', 1, 12, None)


attribAction_894170243889120025 = pycopia.XML.POM.XMLAttribute(u'action', pycopia.XML.POM.Enumeration((u'signal-none', u'signal-low', u'signal-medium', u'signal-high', u'delete')), 13, u'signal-medium')




# 
# Service Indication (SI) Document Type Definition.
# 
# Copyright Wireless Application Protocol Forum Ltd., 1998,1999.
#                       All rights reserved.  
# 
# SI is an XML language.  Typical usage:
#    <?xml version="1.0"?>
#    <!DOCTYPE si PUBLIC "-//WAPFORUM//DTD SI 1.0//EN"
#                 "http://www.wapforum.org/DTD/si.dtd">
#    <si>
#    ...
#    </si>
# 
# Terms and conditions of use are available from the Wireless 
# Application Protocol Forum Ltd. web site at
# http://www.wapforum.org/docs/copyright.htm.
# 


#  ISO date and time 


#  URI designating a 
#                                               hypertext node    


# ====================== The SI Element ======================


class Si(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'si'



_Root = Si



# ================== The indication Element ==================


class Indication(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'action': attribAction_894170243889120025, 
         u'si-expires': attribSi_expires_2496959613638388889, 
         u'href': attribHref_2430637454403731329, 
         u'created': attribCreated_4009362612254311225, 
         u'si-id': attribSi_id_809765079235731441, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	KWATTRIBUTES = {
         'action': attribAction_894170243889120025, 
         'href': attribHref_2430637454403731329, 
         'si_expires': attribSi_expires_2496959613638388889, 
         'si_id': attribSi_id_809765079235731441, 
         'created': attribCreated_4009362612254311225, 
         }
	_name = u'indication'


# ===================== The INFO Element =====================


class Info(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'info'


class Item(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'class': attribClass_2331018730345177744, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	KWATTRIBUTES = {
         'class_': attribClass_2331018730345177744, 
         }
	_name = u'item'


# 
# Copyright Wireless Application Protocol Forum Ltd., 1998,1999.
#                       All rights reserved.  
# 


GENERAL_ENTITIES = {}

# Cache for dynamic classes for this dtd.


_CLASSCACHE = {}


