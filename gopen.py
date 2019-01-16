from contextlib import contextmanager


@contextmanager
def gopen(source):
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
                ftype = filetype(source)
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


def filetype(filename):
    import magic
    return magic.from_file(filename).split()[0]
