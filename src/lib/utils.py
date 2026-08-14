import re

import jsonpath
import requests


def replace_dynamic_vars(value, vars):
    to_replace = re.findall("{{(.*?)}}", value)
    for x in to_replace:
        value = value.replace(x, vars[x])
    value = value.replace("{{", "").replace("}}", "")
    return value
    


def send_request(request):
    return requests.request(request.method, request.url)


def extract_values(keep, json, vars):
    for k in keep:
        vars[k] = str(jsonpath.findall(keep[k], json)[0])
