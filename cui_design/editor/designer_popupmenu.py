#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Designer popup menu.
"""

import collections
import asciimatics.widgets
import asciimatics.screen

__version__ = (0, 0, 0, 1)

DEFAULT_POPUPMENU_THEME = collections.defaultdict(
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
                         asciimatics.screen.Screen.COLOUR_GREEN),
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


class cuiPopupMenu(asciimatics.widgets.PopupMenu):
    """
    Designer popup menu.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(cuiPopupMenu, self).__init__(*args, **kwargs)
        # popup_menu._has_border = True
        self._has_shadow = True
        # popup_menu.canvas.width += 2
        # popup_menu.canvas.height += 2

        self.palette = DEFAULT_POPUPMENU_THEME
        if self._scroll_bar:
            self._scroll_bar.palette = self.palette
