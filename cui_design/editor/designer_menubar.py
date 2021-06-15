#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Designer menubar.
"""

import collections
import asciimatics.widgets
import asciimatics.screen

__version__ = (0, 0, 0, 1)

DEFAULT_MENUBAR_THEME = collections.defaultdict(
    lambda: (asciimatics.screen.Screen.COLOUR_BLACK,
             asciimatics.screen.Screen.A_NORMAL,
             asciimatics.screen.Screen.COLOUR_WHITE),
    {
        'label': (asciimatics.screen.Screen.COLOUR_BLACK,
                  asciimatics.screen.Screen.A_BOLD,
                  asciimatics.screen.Screen.COLOUR_WHITE),
        'title': (asciimatics.screen.Screen.COLOUR_BLACK,
                  asciimatics.screen.Screen.A_BOLD,
                  asciimatics.screen.Screen.COLOUR_WHITE),
        'focus_edit_text': (asciimatics.screen.Screen.COLOUR_BLACK,
                            asciimatics.screen.Screen.A_BOLD,
                            asciimatics.screen.Screen.COLOUR_WHITE),
        'focus_field': (asciimatics.screen.Screen.COLOUR_BLACK,
                        asciimatics.screen.Screen.A_BOLD,
                        asciimatics.screen.Screen.COLOUR_WHITE),
        'focus_button': (asciimatics.screen.Screen.COLOUR_BLACK,
                         asciimatics.screen.Screen.A_BOLD,
                         asciimatics.screen.Screen.COLOUR_YELLOW),
        'focus_control': (asciimatics.screen.Screen.COLOUR_BLACK,
                          asciimatics.screen.Screen.A_BOLD,
                          asciimatics.screen.Screen.COLOUR_WHITE),
        'disabled': (asciimatics.screen.Screen.COLOUR_BLACK,
                     asciimatics.screen.Screen.A_BOLD,
                     asciimatics.screen.Screen.COLOUR_WHITE),
        'shadow': (asciimatics.screen.Screen.COLOUR_WHITE,
                   None,
                   asciimatics.screen.Screen.COLOUR_BLACK),
    }
)


class cuiDesignerMenubar(asciimatics.widgets.Frame):
    """
    Designer menubar.
    """
    def __init__(self, screen):
        """
        Constructor.

        :param screen: Screen.
        """
        super(cuiDesignerMenubar, self).__init__(screen,
                                                 height=1,
                                                 width=screen.width,
                                                 x=0, y=0,
                                                 has_border=False,
                                                 # data=form_data,
                                                 has_shadow=False,
                                                 name='DesignerMenubar')
        self.palette = DEFAULT_MENUBAR_THEME
        if self._scroll_bar:
            self._scroll_bar.palette = self.palette
