"""Provides gopen function."""
from contextlib import contextmanager


@contextmanager
def gopen(source):
    """Context manager for readable files.

    Usage:
    >>> import gopen
    >>> with gopen.gopen(`source`) as f:
    >>>     <do something with f>
    `source` can be: a file-like object, a valid filename, a file descriptor.
    If `source` is a file-like object, do not close it.
    """
    import io
    import six
    import codecs

    if hasattr(source, 'read'):
        yield source  # yield the handle without closing
    else:  # set handle or raise an exception
        if isinstance(source, int):  # file descriptor
            try:
                handle = io.open(source, 'r', closefd=False)
            except OSError:
                raise OSError('Cant open file file descriptor %s', source)
        elif isinstance(source, six.string_types):  # a filename
            try:
                ftype = _filetype(source)
            except IOError:
                raise IOError('File: %s not found', source)
            else:
                if ftype == 'ASCII':
                    handle = open(source, 'r')
                elif ftype == 'gzip':
                    import gzip
                    handle = codecs.getreader('utf-8')(gzip.open(source, 'r'))
                elif ftype == 'bzip2':
                    from bz2 import BZ2File
                    handle = codecs.getreader('utf-8')(BZ2File(source, 'r'))
                else:
                    raise TypeError('Invalid filetype (%s)' % ftype)
        else:
            raise TypeError('Expected {str, int, file-like}, '
                            'got %s' % type(source))
        yield handle
        handle.close()


def read(source):
    with gopen(source) as f:
        for line in f:
            yield line


def _filetype(filename):
    """Return the file type of `filename`."""
    import magic  # pylint: disable=import-error
    return magic.from_file(filename).split()[0]
