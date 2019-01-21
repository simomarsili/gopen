import os
import pytest
import gopen
STRING = 'qux\nquux\nquuz\n'


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
    else:
        test_dir = os.path.join(cwd, 'tests')
        if os.path.exists(test_dir):
            return test_dir


@pytest.fixture()
def tmp_file():
    import tempfile
    import os
    fd, fpath = tempfile.mkstemp(text=True)
    with open(fpath, 'w') as f:
        print(STRING, file=f, end='')
    yield {'fd': fd, 'file': fpath}
    os.close(fd)
    os.remove(fpath)


def test_basic(tmp_file):
    file_path = tmp_file['file']
    with gopen.gopen(file_path) as fp:
        assert fp.read() == STRING


def test_file_descriptor(tmp_file):
    fd = tmp_file['fd']
    with gopen.gopen(fd) as fp:
        assert fp.read() == STRING
