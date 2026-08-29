from lib.objective import Objective


class Suite:
    vars: dict
    objectives: list[Objective]

    def run(self):
        for objective in self.objectives:
            for controller in objective.controllers:
                controller.execute(self.vars)
