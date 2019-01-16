=====
gopen
=====
Provides a factory function for "with" context managers
for readable file objects::

  >>> with gopen.gopen(source) as f:
  >>>     <do something with f>

No side effects: if `source` is file-like and not closed, it won't be closed.
