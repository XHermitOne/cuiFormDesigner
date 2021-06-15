#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Designer resource editor control.
"""

import asciimatics.widgets

from . import resource_browser
from . import property_editor

__version__ = (0, 0, 0, 1)


class cuiResourceEditor(asciimatics.widgets.Frame):
    def __init__(self, screen, width, height, resource=None):
        """
        Constructor.

        :param screen: Screen objects.
        :param resource: Resource data struct.
        """
        super(cuiResourceEditor, self).__init__(
            screen, height, width, has_border=True, name='ResourceEditor')

        # Create the (very simple) form layout...
        layout = asciimatics.widgets.Layout([20], fill_frame=True)
        self.add_layout(layout)

        self._resource_browser = resource_browser.cuiResourceBrowser(20,
                                                                     resource,
                                                                     name='ResourceBrowser')
                                                                     # on_select=self.popup,
                                                                     # on_change=self.details)
        self._property_editor = property_editor.cuiPropertyEditor(20,
                                                                  resource,
                                                                  name='PropertyEditor')

        layout.add_widget(self._resource_browser)
        layout.add_widget(asciimatics.widgets.Divider())
        layout.add_widget(self._property_editor)

        # Prepare the Frame for use
        self.fix()

