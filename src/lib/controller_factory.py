from lib.controller import SimpleController


def get_controller_by_type(controllerType):
    controllerMap = {
        "simple": SimpleController()
    }

    return controllerMap[controllerType]