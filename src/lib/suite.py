from lib.controller import Controller
from lib.utils import extract_values, send_request


class Suite:
    vars: dict
    controllers: list[Controller]

    def run(self):
        for controller in self.controllers:
            controller.request.prepare_before_run(self.vars)

            response = send_request(controller.request)

            extract_values(controller.keep, response.json(), self.vars)
