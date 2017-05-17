from collections import namedtuple

LookupScheme = namedtuple('LookupScheme', ['internal', 'central', 'regional'])

LookupScheme.__new__.__defaults__ = (False,) * len(LookupScheme._fields)