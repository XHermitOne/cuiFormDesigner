#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Designer property editor control.
"""

import asciimatics.widgets

# from ..util import

__version__ = (0, 0, 0, 1)


class cuiPropertyEditor(asciimatics.widgets.MultiColumnListBox):
    """
    Designer property editor control.
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
        super(cuiPropertyEditor, self).__init__(
            height,
            [0, '>8', '>14'],
            [],
            titles=['Name', 'Value', 'button'],
            name=name)
            # name=name,
            # on_select=self._on_selection if on_select is None else on_select,
            # on_change=self._on_change if on_change is None else on_change)

        self._resource = resource

        self._initialized = False

    def update(self, frame_no):
        """
        Update control.

        :param frame_no:
        :return:
        """
        # Defer initial population until we first display the widget in order to avoid race
        # conditions in the Frame that may be using this widget.
        if not self._initialized:
            list_view = self.resource2list(self._resource)
            self.options = list_view
            self._initialized = True
        super(cuiPropertyEditor, self).update(frame_no)

    def resource2list(self, resource=None):
        """
        Convert resource struct to list data.

        :param resource: Resource struct.
        :return: List data struct.
        """
        if resource is None:
            resource = self._resource

        if not resource:
            return list()

        list_view = []
        try:
            spc_names = [name for name in resource.keys() if not name.startswith('_')]
            for name in spc_names:
                list_item = ([name, resource[name], '...'], name)
                list_view.append(list_item)
        except:
            raise
        return list_view
