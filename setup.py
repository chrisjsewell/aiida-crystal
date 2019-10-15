#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup."""

import io
from importlib import import_module
from setuptools import setup, find_packages

with io.open('README.md') as readme:
    description = readme.read()

setup(
    name='aiida-crystal',
    version="0.1.0",
    description='AiiDA plugin for CRYSTAL17',
    long_description=description,
    long_description_content_type='text/markdown',
    install_requires=[],
    license='MIT',
    author='Chris Sewell',
    author_email='chrisj_sewell@hotmail.com',
    url="https://aiida-crystal17.readthedocs.io/",
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Physics',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
    ],
    keywords='python, parser, crystal, aiida',
    zip_safe=True,
    packages=find_packages(),
)
