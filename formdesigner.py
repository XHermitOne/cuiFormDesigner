#!/usr/bin/env python3

"""
Form designer main function module.
"""

import sys

import asciimatics.widgets
import asciimatics.event
import asciimatics.screen
import asciimatics.scene
import asciimatics.effects
import asciimatics.exceptions
import asciimatics.constants

from cui_design.editor import designer_menubar
from cui_design.editor import resource_editor

# MOVE_KEY_CODES = (asciimatics.screen.Screen.KEY_LEFT,
#                   asciimatics.screen.Screen.KEY_RIGHT,
#                   asciimatics.screen.Screen.KEY_UP,
#                   asciimatics.screen.Screen.KEY_DOWN)


# class cuiFrame(asciimatics.widgets.Frame):
#     def __init__(self, screen):
#         super(cuiFrame, self).__init__(screen,
#                                        int(screen.height * 2 // 3),
#                                        int(screen.width * 2 // 3),
#                                        # data=form_data,
#                                        has_shadow=True,
#                                        name='Form')
#
#         self._resize_mode = False
#
#         # self.fix()
#
#     def process_event(self, event):
#         """
#         Event handler.
#         """
#         # Handle dynamic pop-ups now.
#         # if (event is not None and isinstance(event, asciimatics.event.MouseEvent) and
#         #         event.buttons == asciimatics.event.MouseEvent.DOUBLE_CLICK):
#         #     # By processing the double-click before Frame handling, we have absolute coordinates.
#         #     options = [
#         #         ('Default', self._set_default),
#         #         ('Green', self._set_green),
#         #         ('Monochrome', self._set_mono),
#         #         ('Bright', self._set_bright),
#         #     ]
#         #     if self.screen.colours >= 256:
#         #         options.append(('Red/white', self._set_tlj))
#         #     self._scene.add_effect(asciimatics.widgets.PopupMenu(self.screen, options, event.x, event.y))
#         #     event = None
#
#         move_code = None
#         if event is not None and isinstance(event, asciimatics.event.KeyboardEvent):
#             if event.key_code == asciimatics.screen.Screen.KEY_CONTROL:
#                 self._resize_mode = not self._resize_mode
#
#             elif event.key_code in MOVE_KEY_CODES:
#                 move_code = event.key_code
#
#         if self._resize_mode:
#             if move_code == asciimatics.screen.Screen.KEY_LEFT:
#                 # self.move_to(self._canvas.width)
#                 self.canvas.width = self.canvas.width - 1
#             elif move_code == asciimatics.screen.Screen.KEY_RIGHT:
#                 self.canvas.width = self.canvas.width + 1
#             elif move_code == asciimatics.screen.Screen.KEY_UP:
#                 self.canvas.height = self.canvas.height - 1
#             elif move_code == asciimatics.screen.Screen.KEY_DOWN:
#                 self.canvas.height = self.canvas.height + 1
#         else:
#             if move_code == asciimatics.screen.Screen.KEY_LEFT:
#                 self.canvas._dx = self.canvas._dx - 1
#             elif move_code == asciimatics.screen.Screen.KEY_RIGHT:
#                 self.canvas._dx = self.canvas._dx + 1
#             elif move_code == asciimatics.screen.Screen.KEY_UP:
#                 self.canvas._dy = self.canvas._dy - 1
#             elif move_code == asciimatics.screen.Screen.KEY_DOWN:
#                 self.canvas._dy = self.canvas._dy + 1
#
#         if move_code:
#             self.canvas.refresh()
#         # else:
#         #     # Pass any other event on to the Frame and contained widgets.
#         #     return super(cuiFrame, self).process_event(event)


def run(screen, scene):
    screen.play([asciimatics.scene.Scene([
        asciimatics.effects.Background(screen),
        resource_editor.cuiResourceEditor(screen, height=screen.height-2),
        designer_menubar.cuiDesignerMenubar(screen),
        # cuiFrame(screen),
    ], -1)], stop_on_resize=True, start_scene=scene, allow_int=True)


def main():
    last_scene = None
    while True:
        try:
            asciimatics.screen.Screen.wrapper(run, catch_interrupt=False, arguments=[last_scene])
            sys.exit(0)
        except asciimatics.exceptions.ResizeScreenError as error:
            last_scene = error.scene


if __name__ == '__main__':
    main()
