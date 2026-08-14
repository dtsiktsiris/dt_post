from abc import ABC

from lib.request import Request


class Controller(ABC):
    name: str
    type: str
    request: Request
    keep: dict


class SimpleController(Controller):


    def __repr__(self):
        return f"{self.__class__!s}({self.__dict__!r})"
