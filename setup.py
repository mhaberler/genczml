#!/usr/bin/env python

import sys

from setuptools import setup # type: ignore

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')

# with open('README.md') as f:
#     long_description = f.read()

setup(
    name='genczml',
    #version=bfc2gpx.__version__,
    description='Convert flight tracks and trajectories into CZML',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # license='Apache License, Version 2.0',
    author='Michael Haberler',
    author_email='haberlerm@gmail.com',
    url='https://github.com/mhaberler/genczml',
    packages=['cesium_support', 'orient' ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    scripts=['genczml', 'heidi'],
)
