# -*- coding: utf-8 -*-
import os.path as op

import sphinx_rtd_theme


__version__ = '0.1.0.dev0'
VERSION = __version__


def get_html_theme_path():
    """
    Returns path to directory containing this package's theme.

    This is designed to be used when setting the ``html_theme_path``
    option within Sphinx's ``conf.py`` file.
    """
    return [op.abspath(op.join(op.dirname(__file__), "theme")),
            sphinx_rtd_theme.get_html_theme_path()]


def default_sidebars():
    """
    Returns a dictionary mapping for the templates used to render the
    sidebar on the index page and sub-pages.
    """
    return {
        '**': ['localtoc.html', 'relations.html', 'searchbox.html'],
        'index': ['searchbox.html'],
        'search': [],
    }
