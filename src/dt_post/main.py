import json
import jsonpath
import re
import requests

from lib.controller import SimpleController
from lib.loaders import load_from_json


def replace_vars(request):
    to_replace = re.findall("{{.+}}", request.url)
    for x in to_replace:
        x_without_brackets = x[2:-2]
        request.url = request.url.replace(x, vars[x_without_brackets])
    return request


def send_request(request):
    if request.method == "GET":
        return requests.get(request.url)


def extract_values(keep, json, vars):
    for k in keep:
        vars[k] = str(jsonpath.findall(keep[k], json)[0])


def main() -> None:

    with open("suite_env.json", "r") as file:
        loaded_data = json.load(file)
        global vars
        vars = loaded_data["vars"]

    with open("suite.json", "r") as file:
        loaded_data = json.load(file)

        controllers = load_from_json(loaded_data)

    for controller in controllers:
        controller.request = replace_vars(controller.request)

        response = send_request(controller.request)

        extract_values(controller.keep, response.json(), vars)

    print(vars)


