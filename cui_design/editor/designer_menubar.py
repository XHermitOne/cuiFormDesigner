#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Designer menubar.
"""

import collections
import asciimatics.widgets
import asciimatics.screen
import asciimatics.exceptions

from . import designer_popupmenu

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

        layout = asciimatics.widgets.Layout([1, 80])
        self.add_layout(layout)

        self._file_button = asciimatics.widgets.Button(text=u'File', on_click=self.onFileButtonClick)
        layout.add_widget(self._file_button, 0)

        # Prepare the Frame for use
        self.fix()

    def onFileButtonClick(self):
        """
        File button click handler.
        """
        menu_items = [('New', self.onNewFileMenuItemSelected),
                      ('Load...', self.onLoadFileMenuItemSelected),
                      ('Save', self.onSaveFileMenuItemSelected),
                      ('Save As...', self.onSaveAsFileMenuItemSelected),
                      # asciimatics.widgets.Divider(),
                      ('Exit', self.onExitFileMenuItemSelected),
                      ]
        popup_menu = designer_popupmenu.cuiPopupMenu(screen=self.screen, menu_items=menu_items,
                                                     x=self._file_button._x,
                                                     y=self._file_button._y + 1)

        self._scene.add_effect(popup_menu)

    def onNewFileMenuItemSelected(self):
        """
        New file menuitem handler.
        """
        menu_items = [('Form', self.onNewFormMenuItemSelected),
                      ]
        popup_menu = designer_popupmenu.cuiPopupMenu(screen=self.screen, menu_items=menu_items,
                                                     x=0,
                                                     y=1)

        self._scene.add_effect(popup_menu)

    def onNewFormMenuItemSelected(self):
        """
        New form menuitem handler.
        """
        pass

    def onLoadFileMenuItemSelected(self):
        """
        Load file menuitem handler.
        """
        # print('OK')
        pass

    def onSaveFileMenuItemSelected(self):
        """
        Save file menuitem handler.
        """
        # print('OK')
        pass

    def onSaveAsFileMenuItemSelected(self):
        """
        Save as... file menuitem handler.
        """
        # print('OK')
        pass

    def onExitFileMenuItemSelected(self):
        """
        Exit file menuitem handler.
        """
        raise asciimatics.exceptions.StopApplication('User requested exit')
