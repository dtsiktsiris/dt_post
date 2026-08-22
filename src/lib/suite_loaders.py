import json

from lib.loaders import load_from_json
from lib.suite import Suite


@staticmethod
def load_from_json_files(suiteFile, envFile) -> Suite:
    suite = Suite()
    with open(envFile, "r") as file:
        loaded_data = json.load(file)

        suite.vars = loaded_data["vars"]

    with open(suiteFile, "r") as file:
        loaded_data = json.load(file)

        suite.controllers = load_from_json(loaded_data)

    return suite