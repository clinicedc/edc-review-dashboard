# -*- coding: utf-8 -*-
import os
from os.path import abspath, dirname, join, normpath

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), "VERSION")) as f:
    VERSION = f.read()

# allow setup.py to be run from any path
os.chdir(normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="edc-review-dashboard",
    version=VERSION,
    author="Erik van Widenfelt",
    author_email="ew2789@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/clinicedc/edc-review-dashboard",
    license="GPL license, see LICENSE",
    description="A dashboard with direct links to a subject's CRFs and Requisitions.",
    long_description=README,
    zip_safe=False,
    keywords="django edc review dashboard",
    install_requires=[],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
)
