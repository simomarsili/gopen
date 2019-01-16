import gopen
txt = 'qux\nquux\nquuz\n'


def test_basic():
    with gopen.gopen('txt') as fp:
        assert fp.read() == txt


def test_gzip():
    with gopen.gopen('txt.gz') as fp:
        assert fp.read() == txt


def test_bzip2():
    with gopen.gopen('txt.bzip2') as fp:
        assert fp.read() == txt
