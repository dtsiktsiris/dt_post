from abc import ABC

from requests import Response

from lib.request import Request
from lib.utils import extract_values, send_request


class Controller(ABC):
    name: str
    type: str
    request: Request
    keep: dict
    response: Response | None

    def replace_dynamic_values(self, vars):
        self.request.prepare_before_run(vars)

    def keep_values(self, vars):
        extract_values(self.keep, self.response.json(), vars)


class SimpleController(Controller):

    def execute(self):
        self.response = send_request(self.request)
        print('----------')
        print(self.response.json())

    def __repr__(self):
        return f"{self.__class__!s}({self.__dict__!r})"
