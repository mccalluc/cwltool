# Stubs for galaxy.util.bunch (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Bunch:
    def __init__(self, **kwds) -> None: ...
    def dict(self): ...
    def get(self, key, default: Optional[Any] = ...): ...
    def __iter__(self): ...
    def items(self): ...
    def keys(self): ...
    def values(self): ...
    def __nonzero__(self): ...
    def __setitem__(self, k, v): ...
    def __contains__(self, item): ...
