import json

from lib.loaders import load_from_json
from lib.suite import Suite


def main() -> None:

    suite = Suite()

    with open("suite_env.json", "r") as file:
        loaded_data = json.load(file)

        suite.vars = loaded_data["vars"]

    with open("suite.json", "r") as file:
        loaded_data = json.load(file)

        suite.controllers = load_from_json(loaded_data)

    suite.run()

    # print(suite.vars)
