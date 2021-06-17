#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Form widget specification.
"""

__version__ = (0, 0, 0, 1)

WIDGET_TYPE = 'Form'

FORM_SPC = {
    'name': 'default',
    'type': WIDGET_TYPE,
    'description': '',
    'activate': True,

    '_children_': [],

    'pos': (-1, -1),
    'size': (-1, -1),
    'foreground_colour': None,
    'background_colour': None,

    'title': '',

    'has_shadow': True,

    '__package__': u'Widgets',
    '__parent__': None,
    '__doc__': None,
    '__content__': ('Button', ),
    '__edit__': {
    },
    '__help__': {
        'pos': u'Form position',
        'size': u'Form size',
        'foreground_colour': u'Foreground colour',
        'background_colour': u'Background colour',
        'title': u'Form title',
        'has_shadow': u'Has form shadow?',
    },
}

SPC = FORM_SPC
