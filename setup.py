# -*- coding: utf-8 -*-
# python setup.py register sdist upload
# coding: utf-8
from setuptools import setup, find_packages
from akilib import * 

setup(
    name = 'akilib',
    version = '2.0.9',
    url="https://github.com/nonNoise/akilib",
    keywords = ('Edison','Raspberry','IoT','akilib'),
    description = 'This Library is Hardware Library. and You can buy parts in Japan Akihabara .',
    license = 'MIT License',
    install_requires = [],
    packages=['akilib','akilib/edison','akilib/raspberrypi'],
    author = ' Yuta KItagami',
    author_email = 'kitagami@artifactnoise.com',
    platforms = ['Linux'],
)



 
