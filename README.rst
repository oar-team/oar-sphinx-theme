OAR Documentation Theme
=======================

OAR Documentation Theme is a Python package providing Sphinx theme for the OAR documentation at http://oar.imag.fr/docs/2.5/

This project is based on `JuliaDoc`_, a sphinx theme for the Julia language documentation.

.. _`JuliaDoc`: https://github.com/JuliaLang/JuliaDoc

Installation
------------

You can install, upgrade, uninstall ``oar-sphinx-theme`` with these commands

.. code:: bash

  $ pip install [--user] oar-sphinx-theme
  $ pip install [--user] --upgrade oar-sphinx-theme
  $ pip uninstall oar-sphinx-theme

Or from git (last development version)

.. code:: bash

  $ pip install git+https://github.com/oar-team/oar-sphinx-theme.git

Once installed you should change your Sphinx ``conf.py`` to include

.. code:: python

    import oar_theme

    html_theme = 'oar'
    html_theme_path = oar_theme.get_html_theme_path()
    html_sidebars = oar_theme.default_sidebars()
