#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os.path as op


from codecs import open
from setuptools import setup, find_packages


def read(fname):
    ''' Return the file content. '''
    here = op.abspath(op.dirname(__file__))
    with open(op.join(here, fname), 'r', 'utf-8') as fd:
        return fd.read()

readme = read('README.rst')
changelog = read('CHANGES.rst').replace('.. :changelog:', '')

requirements = [
    "sphinx_rtd_theme",
]

version = ''
version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                    read(op.join('oar_theme', '__init__.py')),
                    re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


setup(
    name='oar-sphinx-theme',
    author="Salem Harrache",
    author_email='salem.harrache@harrache.info',
    version=version,
    url='https://github.com/oar-team/oar-sphinx-theme',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    description="OAR Documentation Theme is a Python package providing Sphinx theme for the OAR documentation at http://oar.imag.fr/docs/2.5/",
    long_description=readme + '\n\n' + changelog,
    keywords=' sphinx_rtd_theme.get_html_theme_path()',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
    ],
)
