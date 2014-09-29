#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from os import path
from setuptools import setup


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


setup(
    name='django-jenkins-extends',
    version='0.0.1',
    author='Witold Gren',
    author_email='witold.gren@gmail.com',
    description='Package add to django-jenkins taks pylint custom plugin',
    long_description=read(path.abspath(path.join(path.dirname(__file__), 'README.md'))),
    license='LGPL',
    platforms=['Any'],
    keywords=['hudson', 'jenkins', 'django', 'pylint'],
    url='http://github.com/witold-gren/django-jenkins-extends',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=[
        'Django>=1.6',
        'django_jenkins',
    ],
    packages=['django_jenkins_extends',],
    zip_safe=False,
    include_package_data=True
)