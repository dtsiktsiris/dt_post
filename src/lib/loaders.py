from lib.controller_factory import get_controller_by_type
from lib.request import Request


def load_from_json(jsonSuite):
    controllers = []

    for controller in jsonSuite["controllers"]:
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

    return controllers
