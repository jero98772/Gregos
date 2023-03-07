#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Gregos - by [jero98772,camilo,GianSz,camilo_alvarez,igatsi]
from setuptools import setup, find_packages
setup(
	name='Gregos',
	version='1.0.0',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772,camilo,GianSz,camilo_alvarez,igatsi',
	description='',
	url='https://github.com/jero98772/Gregos',
	packages=find_packages(),
    install_requires=['Flask', 'chess', 'gtts','pandas'],
    include_package_data=True,
	)