#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Designer resource editor control.
"""

import collections
import asciimatics.widgets
import asciimatics.screen

from . import resource_browser
from . import property_editor

__version__ = (0, 0, 0, 1)

DEFAULT_RESOURCE_EDITOR_THEME = collections.defaultdict(
    lambda: (asciimatics.screen.Screen.COLOUR_BLACK,
             asciimatics.screen.Screen.A_NORMAL,
             asciimatics.screen.Screen.COLOUR_CYAN),
    {
        'label': (asciimatics.screen.Screen.COLOUR_BLACK,
                  asciimatics.screen.Screen.A_BOLD,
                  asciimatics.screen.Screen.COLOUR_CYAN),
        'title': (asciimatics.screen.Screen.COLOUR_BLACK,
                  asciimatics.screen.Screen.A_BOLD,
                  asciimatics.screen.Screen.COLOUR_CYAN),
        'focus_edit_text': (asciimatics.screen.Screen.COLOUR_BLACK,
                            asciimatics.screen.Screen.A_BOLD,
                            asciimatics.screen.Screen.COLOUR_CYAN),
        'focus_field': (asciimatics.screen.Screen.COLOUR_BLACK,
                        asciimatics.screen.Screen.A_BOLD,
                        asciimatics.screen.Screen.COLOUR_CYAN),
        'focus_button': (asciimatics.screen.Screen.COLOUR_BLACK,
                         asciimatics.screen.Screen.A_BOLD,
                         asciimatics.screen.Screen.COLOUR_YELLOW),
        'focus_control': (asciimatics.screen.Screen.COLOUR_BLACK,
                          asciimatics.screen.Screen.A_BOLD,
                          asciimatics.screen.Screen.COLOUR_CYAN),
        'disabled': (asciimatics.screen.Screen.COLOUR_BLACK,
                     asciimatics.screen.Screen.A_BOLD,
                     asciimatics.screen.Screen.COLOUR_CYAN),
        'shadow': (asciimatics.screen.Screen.COLOUR_WHITE,
                   None,
                   asciimatics.screen.Screen.COLOUR_BLACK),
    }
)


class cuiResourceEditor(asciimatics.widgets.Frame):
    def __init__(self, screen, width=40, height=50, x=0, y=1, resource=None):
        """
        Constructor.

        :param screen: Screen objects.
        :param resource: Resource data struct.
        """
        super(cuiResourceEditor, self).__init__(
            screen, height, width,
            x=x, y=y, has_border=True, name='ResourceEditor')

        self.palette = DEFAULT_RESOURCE_EDITOR_THEME
        if self._scroll_bar:
            self._scroll_bar.palette = self.palette

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

