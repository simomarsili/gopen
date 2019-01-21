=====
gopen
=====
Tools for reading from "generic" objects.

- pathnames
- integer file descriptors
- readable file objects 
- gzip, bzip2 compressed files

The gopen module provides two functions:

- gopen()
  Provides a factory function for "with" context managers
  for readable file objects::

    >>> with gopen.gopen(source) as f:
    >>>     <do something with f>

- gopen.gread()

If a file descriptor or a file handle is given, it won't be closed.
