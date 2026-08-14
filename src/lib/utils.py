import jsonpath
import requests


def send_request(request):
    return requests.request(request.method, request.url)


def extract_values(keep, json, vars):
    for k in keep:
        vars[k] = str(jsonpath.findall(keep[k], json)[0])
