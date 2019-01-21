=====
gopen
=====
Provides the **gopen.gread()** function. Basic usage::

  >>> from gopen import gread
  >>> lines = gread(source)
  >>> lines
  <generator object gread at 0x7f45752ebf10>

**gread** returns an interator over text input lines.

Valid inputs are: readable file objects,
integer file descriptors, file pathnames.
gzip and bzip2-compressed files will be decompressed on the fly.
No side effects: if a file descriptor or a file handle is given,
it will not be closed.
