#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Widget module.
"""

import asciimatics.widgets
import asciimatics.event
import asciimatics.screen

from .. import widget_proto

__version__ = (0, 0, 0, 1)

MOVE_KEY_CODES = (asciimatics.screen.Screen.KEY_LEFT,
                  asciimatics.screen.Screen.KEY_RIGHT,
                  asciimatics.screen.Screen.KEY_UP,
                  asciimatics.screen.Screen.KEY_DOWN)


class cuiForm(asciimatics.widgets.Frame, widget_proto.cuiWidget):
    """
    Form widget class.
    """
    def __init__(self, parent, resource=None, spc=None, context=None, *args, **kwargs):
        """
        Constructor.

        :param parent:
        :param resource:
        :param spc:
        :param context:
        :param args:
        :param kwargs:
        """
        component_spc = kwargs['spc'] if 'spc' in kwargs else spc.SPC
        widget_proto.cuiWidget.__init__(self, parent=parent, resource=resource, spc=component_spc, context=context)

        screen = parent
        super(cuiForm, self).__init__(screen,
                                      int(screen.height * 2 // 3),
                                      int(screen.width * 2 // 3),
                                      # data=form_data,
                                      has_shadow=True,
                                      name='Form',
                                      *args, **kwargs)

        self._resize_mode = False

        # self.fix()

    def process_event(self, event):
        """
        Event handler.
        """
        # Handle dynamic pop-ups now.
        # if (event is not None and isinstance(event, asciimatics.event.MouseEvent) and
        #         event.buttons == asciimatics.event.MouseEvent.DOUBLE_CLICK):
        #     # By processing the double-click before Frame handling, we have absolute coordinates.
        #     options = [
        #         ('Default', self._set_default),
        #         ('Green', self._set_green),
        #         ('Monochrome', self._set_mono),
        #         ('Bright', self._set_bright),
        #     ]
        #     if self.screen.colours >= 256:
        #         options.append(('Red/white', self._set_tlj))
        #     self._scene.add_effect(asciimatics.widgets.PopupMenu(self.screen, options, event.x, event.y))
        #     event = None

        move_code = None
        if event is not None and isinstance(event, asciimatics.event.KeyboardEvent):
            if event.key_code == asciimatics.screen.Screen.KEY_CONTROL:
                self._resize_mode = not self._resize_mode

            elif event.key_code in MOVE_KEY_CODES:
                move_code = event.key_code

        if self._resize_mode:
            if move_code == asciimatics.screen.Screen.KEY_LEFT:
                # self.move_to(self._canvas.width)
                self.canvas.width = self.canvas.width - 1
            elif move_code == asciimatics.screen.Screen.KEY_RIGHT:
                self.canvas.width = self.canvas.width + 1
            elif move_code == asciimatics.screen.Screen.KEY_UP:
                self.canvas.height = self.canvas.height - 1
            elif move_code == asciimatics.screen.Screen.KEY_DOWN:
                self.canvas.height = self.canvas.height + 1
        else:
            if move_code == asciimatics.screen.Screen.KEY_LEFT:
                self.canvas._dx = self.canvas._dx - 1
            elif move_code == asciimatics.screen.Screen.KEY_RIGHT:
                self.canvas._dx = self.canvas._dx + 1
            elif move_code == asciimatics.screen.Screen.KEY_UP:
                self.canvas._dy = self.canvas._dy - 1
            elif move_code == asciimatics.screen.Screen.KEY_DOWN:
                self.canvas._dy = self.canvas._dy + 1

        if move_code:
            self.canvas.refresh()
        # else:
        #     # Pass any other event on to the Frame and contained widgets.
        #     return super(cuiFrame, self).process_event(event)


WIDGET = cuiForm
