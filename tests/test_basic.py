# -*- coding: utf-8 -*-
"""Tests module."""
# pylint: disable=missing-docstring
import os

import pytest

import gopen

STRING = 'Simple is\nbetter than complex.'


def _compress(path, compressor):
    import subprocess
    extension = {'gzip': '.gz', 'bzip2': '.bz2'}
    if compressor in extension:
        subprocess.check_call('%s %s' % (compressor, path), shell=True)
    else:
        raise ValueError('Possible compressors are: %s, %s' % extension.keys())
    path1 = path + extension[compressor]
    return path1


def _test_dir():
    """Return None is no tests dir."""
    cwd = os.getcwd()
    basename = os.path.basename(cwd)
    if basename == 'tests':
        return cwd

    test_dir = os.path.join(cwd, 'tests')
    if os.path.exists(test_dir):
        return test_dir

    return None


@pytest.fixture()
def tmp_file():
    import tempfile
    fd, fpath = tempfile.mkstemp(text=True)
    with open(fpath, 'w') as f:
        print(STRING, file=f, end='')
    yield {'fd': fd, 'file': fpath}
    os.close(fd)
    os.remove(fpath)


def test_basic(tmp_file):  # pylint: disable=redefined-outer-name
    file_path = tmp_file['file']
    with gopen.readable(file_path) as fp:
        assert fp.read() == STRING


def test_file_descriptor(tmp_file):  # pylint: disable=redefined-outer-name
    fd = tmp_file['fd']
    with gopen.readable(fd) as fp:
        assert fp.read() == STRING
