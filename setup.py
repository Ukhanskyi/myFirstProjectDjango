#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    install_requires=open("requirements.txt").readlines(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
)