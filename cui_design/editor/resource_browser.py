#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Designer resource tree browser control.
"""

import uuid
import asciimatics.widgets

# from ..util import

__version__ = (0, 0, 0, 1)


class cuiResourceBrowser(asciimatics.widgets.MultiColumnListBox):
    """
    Designer resource tree browser control.
    """

    def __init__(self, height, resource, name=None, on_select=None, on_change=None):
        """
        Constructor.

        :param height: The desired height for this widget.
        :param resource: Resource tree data.
        :param name: The name of this widget.
        :param on_select: Optional function that gets called when user selects a file (by pressing
            enter or double-clicking).
        :param on_change: Optional function that gets called on any movement of the selection.
        """
        super(cuiResourceBrowser, self).__init__(
            height,
            [0, '>8', '>14', '>32'],
            [],
            titles=['', 'Name', 'Type', 'Description'],
            name=name)
            # name=name,
            # on_select=self._on_selection if on_select is None else on_select,
            # on_change=self._on_change if on_change is None else on_change)

        self._resource = resource
        # self._root = resource

        # self._in_update = False
        self._initialized = False

    def update(self, frame_no):
        """

        :param frame_no:
        :return:
        """
        # Defer initial population until we first display the widget in order to avoid race
        # conditions in the Frame that may be using this widget.
        if not self._initialized:
            tree_view = self.resource2tree(self._resource)
            self.options = tree_view
            self._initialized = True
        super(cuiResourceBrowser, self).update(frame_no)

    def resource2tree(self, resource=None):
        """
        Convert resource tree to tree data.

        :param resource: Resource struct.
        :return: Tree data struct.
        """
        if resource is None:
            resource = self._resource

        if not resource:
            return list()

        tree_view = []
        try:
            tree_item_id = resource.get('guid', str(uuid.uuid4()))
            if resource['_children_']:
                tree_item = (['|-+', resource['name'], resource['type'], resource['description']], tree_item_id)
                tree_view.append(tree_item)

                for child in resource['_children_']:
                    child_tree_view = self.resource2tree(resource=child)
                    if child_tree_view:
                        tree_view += child_tree_view
            else:
                tree_item = (['|--', resource['name'], resource['type'], resource['description']], tree_item_id)
                tree_view.append(tree_item)
        except:
            raise
        return tree_view
