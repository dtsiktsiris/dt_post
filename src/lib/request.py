import re

from lib.enums import Method


class Request:
    url: str
    method: Method
    body: str | None


    def replace_dynamic_vars(self, vars):
        to_replace = re.findall("{{.+}}", self.url)
        for x in to_replace:
            x_without_brackets = x[2:-2]
            self.url = self.url.replace(x, vars[x_without_brackets])
