import json
import re

import jsonpath
import requests


def replace_dynamic_vars(value, vars):
    to_replace = re.findall("({{.*?}})", value)
    for x in to_replace:
        x_no_curls = x[2:-2]
        if isinstance(vars[x_no_curls], dict):
            value = value.replace('"'+x+'"', json.dumps(vars[x_no_curls]))
        elif isinstance(vars[x_no_curls], int):
            value = value.replace('"'+x+'"', str(vars[x_no_curls]))
        else:
            value = value.replace(x, vars[x_no_curls])
    return value
    


def send_request(request):
    return requests.request(request.method, request.url, json = request.body)


def extract_values(keep, json, vars):
    for k in keep:
        vars[k] = jsonpath.findall(keep[k], json)[0]