from typing import List

from requests import Request

from lib.controller import Controller, SimpleController


def load_from_json(jsonSuite):
    controllers : List[Controller] = list()
    
    for controller in jsonSuite["controllers"]:
        # print(controller)
        tempController = SimpleController()
        tempController.name = controller["name"]
        tempController.type = controller["type"]

        req = Request()
        req.url = controller["request"]["url"]
        req.method = controller["request"]["method"]

        tempController.request = req

        tempController.keep = controller["keep"]

        # print(repr(tempController))
        # print(tempController.request.method)

        controllers.append(tempController)


    return controllers
