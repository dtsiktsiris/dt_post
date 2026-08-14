from lib.enums import Method
from lib.utils import replace_dynamic_vars


class Request:
    url: str
    method: Method
    body: str | None


    def prepare_before_run(self, vars):
        self.url = replace_dynamic_vars(self.url, vars)
