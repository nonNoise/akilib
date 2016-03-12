# -*- coding: utf-8 -*-
# python setup.py register sdist upload
from setuptools import setup

import os
f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name = 'akilib',
    version = '2.0.7',
    url="https://github.com/nonNoise/akilib",
    keywords = ('Edison','Raspberry','IoT','akilib'),
    description = 'This Library is Hardware Library. and You can buy parts in Japan Akihabara .',
    license = 'MIT License',
    install_requires = [],
    long_description=long_description,
    packages=['akilib','akilib/edison','akilib/raspberrypi'],
    author = ' Yuta KItagami',
    author_email = 'kitagami@artifactnoise.com',
    platforms = ['Linux'],
)



 
