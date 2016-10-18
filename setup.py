#! /usr/bin/env python

from setuptools import setup, find_packages

PACKAGE = 'pelicanizer'

setup(
    name=PACKAGE,
    description=(
        "A webserver which automatically display renders of "
        "a pelican repo's different branches."
    ),
    url='https://github.com/nejucomo/{}'.format(PACKAGE),
    license='GPLv3',
    version='0.2.1',
    author='Nathan Wilcox',
    author_email='nejucomo@gmail.com',
    packages=find_packages(),
    install_requires=[
        'twisted >= 13.1',
        'Mock >= 1.0.1',
        ],
    entry_points={
        'console_scripts': [
            '{0} = {0}.main:main'.format(PACKAGE),
            ],
        },
    test_suite='{}.tests'.format(PACKAGE),
    package_data={
        PACKAGE: ['web/static/*'],
        },
    )
