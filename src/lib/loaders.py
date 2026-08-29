from lib.controller_factory import get_controller_by_type
from lib.objective import Objective
from lib.request import Request


def load_from_json(jsonSuite):

    objectives = []

    for objective in jsonSuite:
        tempObjective = Objective()

        tempObjective.name = objective["name"]

        controllers = []

        for controller in objective["controllers"]:
            # print(controller)
            tempController = get_controller_by_type(controller["type"])
            
            tempController.name = controller["name"]
            tempController.type = controller["type"]

            req = Request()
            req.url = controller["request"]["url"]
            req.method = controller["request"]["method"]
            try:
                body = controller["request"]["body"]
                req.body = body
            except KeyError:
                req.body = None

            try:
                headers = controller["request"]["headers"]
                req.headers = headers
            except KeyError:
                req.headers = None

            tempController.request = req

            tempController.keep = controller["keep"]

            controllers.append(tempController)

        tempObjective.controllers = controllers

        objectives.append(tempObjective)

    return objectives
