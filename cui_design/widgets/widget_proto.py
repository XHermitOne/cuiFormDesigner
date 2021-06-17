#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Widget prototype.
"""

from ..util import id_func
from ..util import spc_func
from ..util import log_func

from .. import widgets

__version__ = (0, 0, 0, 1)


class cuiWidget(object):
    """
    Widget prototype. Abstract class.
    """
    def __init__(self, parent=None, resource=None, spc=None, context=None, *args, **kwargs):
        """
        Constructor.

        :param parent: Parent widget.
        :param resource: Object resource.
        :param spc: Widget specification.
        :param context: Object context.
        """
        self._parent = parent
        self._resource = resource
        self._spc = spc
        self._context = context

        self._children = list()

    def getParent(self):
        """
        Get parent widget.
        """
        return self._parent

    def getResource(self):
        """
        Get object resource.
        :return:
        """
        return self._resource

    def getSpc(self):
        """
        Get widget specification.
        """
        return self._spc

    def getContext(self):
        """
        Get object context.
        """
        return self._context

    def getName(self):
        """
        Object name.
        """
        res = self.getResource()
        if isinstance(res, dict):
            return res.get('name', u'Unknown')
        return u'Unknown'

    def getType(self):
        """
        Object type.
        """
        res = self.getResource()
        if isinstance(res, dict):
            return res.get('type', u'Unknown')
        return u'Unknown'

    def getGUID(self):
        """
        Object resource GUID.
        """
        res = self.getResource()
        if isinstance(res, dict):
            return res.get('guid', id_func.NONE_GUID)
        return id_func.NONE_GUID

    def isActivate(self):
        """
        Is activate object?
        :return: True/False.
        """
        return self.getAttribute('activate')

    def getDescription(self):
        """
        Object description.
        """
        res = self.getResource()
        if isinstance(res, dict):
            return res.get('description', u'')
        return u''

    def getAttribute(self, attribute_name):
        """
        Get attribute from resource.

        :param attribute_name: Attribute name.
        :return: Attribute value.
        """
        value = self._resource.get(attribute_name, None) if self._resource else None
        return value

    def isAttributeValue(self, attribute_name):
        """
        Defined attribute value?

        :param attribute_name: Attribute name.
        :return: True/False.
        """
        attr_value = self.getAttribute(attribute_name)
        if isinstance(attr_value, str):
            return attr_value.strip() not in ('None', '')
        return attr_value is not None

    def createChildren(self):
        """
        Create children objects.

        :return: Children list or None if error.
        """
        try:
            res_children = self._resource.get(spc_func.CHILDREN_ATTR_NAME, list())
            # kernel = self.getKernel()
            context = self.getContext()

            self._children = [widgets.COMPONENTS[res_child['type']](parent=self,
                                                                    resource=res_child,
                                                                    context=context) for res_child in res_children]
            return self._children
        except:
            log_func.fatal(u'Error create children obj object <%s : %s>' % (self.getName(), self.getType()))
        return list()

    def getChildren(self):
        """
        Get children objects.
        """
        if self._children is None:
            self._children = self.createChildren()
        return self._children

    def hasChildren(self):
        """
        Has children objects?

        :return: True/False.
        """
        return bool(self._children)

    def hasChild(self, name):
        """
        Is there a child with that name?

        :param name: Child object name.
        :return: True/False.
        """
        res_children = self._resource.get(spc_func.CHILDREN_ATTR_NAME, list())
        return name in [res_child.get('name', None) for res_child in res_children]

    def getChild(self, name):
        """
        Get child object by name.

        :param name: Child object name.
        :return: Child object or None if not found.
        """
        children = self.getChildren()

        for child in children:
            if name == child.getName():
                return child

        log_func.warning(u'Child <%s> not found in <%s : %s>' % (name, self.getName(), self.getType()))
        return None

    def findChild(self, name):
        """
        Find child object recursively by name.

        :param name: Child object name.
        :return: Child object or None if not found.
        """
        children = self.getChildren()

        for child in children:
            if name == child.getName():
                return child

        for child in children:
            if child.hasChildren():
                find_child = child.findChild(name)
                if find_child:
                    return find_child

        return None

    def filterChildrenByClass(self, child_class):
        """
        Filter child list by class.

        :param child_class: Child class.
        :return: Child list of child class.
        """
        children = self.getChildren()
        return [child for child in children if issubclass(child.__class__, child_class)]

    def test(self):
        """
        Test object.

        :return: True/False.
        """
        log_func.warning(u'Not defined test function for component <%s : %s>' % (self.getName(), self.getType()))
        return False
