from abc import ABC
from dataclasses import dataclass

from requests import Request

class Controller(ABC):
    name: str
    type: str
    request: Request
    keep: dict

class SimpleController(Controller):
    pass

    def __repr__(self):
        return f"{self.__class__!s}({self.__dict__!r})"