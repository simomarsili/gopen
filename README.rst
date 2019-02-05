=====
gopen
=====
Provides the **gopen.readable()** and **gopen.gread()** functions.

**readable(source)** returns a context manager that supports `with` statements::

  >>> with gopen.readable(source) as f:
  >>>     <read from f>

**gread(source)** returns an interator over input lines::

  >>> from gopen import gread
  >>> lines = gread(source)
  >>> lines
  <generator object gread at 0x7f45752ebf10>

`<source>` can be: a readable file object, a file descriptor and
a file pathname.
gzip and bzip2-compressed files will be decompressed on the fly.
No side effects: if a file descriptor or a file handle is given,
it will not be closed.
