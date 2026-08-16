import json

from lib.enums import Method
from lib.utils import replace_dynamic_vars


class Request:
    url: str
    method: Method
    body: dict | None


    def prepare_before_run(self, vars):
        self.url = replace_dynamic_vars(self.url, vars)
        if self.body is not None:

            tempBody = json.dumps(self.body)
            tempBody = replace_dynamic_vars(tempBody, vars)
            print(tempBody)
            print(json.loads(tempBody))
            self.body = json.loads(tempBody)
