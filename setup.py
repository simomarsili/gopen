# -*- coding: utf-8 -*-
from os import path
from setuptools import setup, find_packages

NAME = 'gopen'
VERSION_FILE = 'version.json'
SETUP_REQUIRES = []
INSTALL_REQUIRES = ['six', 'python-magic']
EXTRAS_REQUIRES = {'test': ['pytest', 'pytest-pep8']}


def get_version(source):
    """ Retrieve version number."""
    import json
    with open(source, 'r') as fp:
        version_data = json.load(fp)
    try:
        return version_data['version']
    except KeyError:
        # no version number in version.json
        raise KeyError("check version file: no version number")


def get_long_description(here):
    """Get the long description from the README file."""
    import codecs
    with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as _rf:
        return _rf.read()


HERE = path.abspath(path.dirname(__file__))
VERSION = get_version(path.join(HERE, VERSION_FILE))
LONG_DESCRIPTION = get_long_description(HERE)

setup(
    name=NAME,
    version=VERSION,
    description='Generic opener',
    long_description=LONG_DESCRIPTION,
    author='Simone Marsili',
    author_email='simo.marsili@gmail.com',
    url='https://github.com/simomarsili/gopen',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # packages=['skmsa'],
    package_data={'':
                  ['LICENSE.txt',
                   'README.md',
                   'requirements.txt']},
    include_package_data=True,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRES,
    license='BSD 3-Clause',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
