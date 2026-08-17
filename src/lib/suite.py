from lib.controller import Controller
from lib.utils import extract_values, send_request


class Suite:
    vars: dict
    controllers: list[Controller]

    def run(self):
        for controller in self.controllers:
            controller.replace_dynamic_values(self.vars)

            controller.execute()

            controller.keep_values(self.vars)
