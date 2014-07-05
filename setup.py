#!/bin/env python
# -*- coding: utf-8 -*-

'Django package for bootstrap-fileinput:' \
    ' An enhanced HTML 5 file input for Bootstrap 3.x with file preview,' \
    ' multiple selection, and more features.'


from setuptools import setup

setup(
    name='django-bootstrap-fileinput',
    version='1.6.0',
    url='http://plugins.krajee.com/file-input',
    description=globals()['__doc__'],
    author='Kartik Visweswaran',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    keywords=['django', 'bootstrap'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_bootstrap_fileinput'],
    package_data={'django_bootstrap_fileinput':
                  ['static/django_bootstrap_fileinput/js/*.js',
                   'static/django_bootstrap_fileinput/css/*.css',
                   'static/django_bootstrap_fileinput/img*.gif']}
)
