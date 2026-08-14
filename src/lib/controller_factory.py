from lib.controller import SimpleController


def get_controller_by_type(controllerType):
    contrellerMap = {
        "simple": SimpleController()
    }

    return contrellerMap[controllerType]