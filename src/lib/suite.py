from lib.controller import Controller


class Suite:
    vars: dict
    controllers: list[Controller]

    def run(self):
        for controller in self.controllers:
            controller.execute(self.vars)
