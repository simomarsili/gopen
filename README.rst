=====
gopen
=====
Tools for reading text from:

- readable file objects 
- pathnames
- integer file descriptors
- gzip, bzip2 compressed files

using a common interface.

The gopen module provides two functions:

- gopen()
  Provides a factory function for "with" context managers
  for readable file objects::

    >>> with gopen.gopen(source) as f:
    >>>     <do something with f>

- gopen.gread()

No side effects: if a file descriptor or a file handle is given,
it will not be closed.
