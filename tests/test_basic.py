import os
import gopen
STRING = 'qux\nquux\nquuz\n'


def _test_dir():
    """Return None is no tests dir."""
    cwd = os.getcwd()
    basename = os.path.basename(cwd)
    if basename == 'tests':
        return cwd
    else:
        tests_dir = os.path.join(cwd, 'tests')
        if os.path.exists(tests_dir):
            return tests_dir


def _check_content(source):
    file_name = os.path.join(_tests_dir(), source)
    with gopen.gopen(file_name) as fp:
        assert fp.read() == STRING


def test_basic():
    _check_content('txt')


def test_gzip():
    _check_content('txt.gz')


def test_bzip2():
    _check_content('txt.gz')


def test_file_descriptor():
    import tempfile
    import os
    fd, fpath = tempfile.mkstemp(text=True)
    with open(fpath, 'w') as f:
        print('foo', file=f, end='')
    with gopen.gopen(fd) as fp:
        assert fp.read() == 'foo'
    os.close(fd)
    os.remove(fpath)

