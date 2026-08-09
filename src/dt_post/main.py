import yaml
import re
import requests
import jsonpath


def replace_vars(request):
    to_replace = re.findall("{{.+}}", request['url'])
    for x in to_replace:
        x_without_brackets = x[2:-2]
        request['url'] = request['url'].replace(x, vars[x_without_brackets])
    return request
    
def send_request(request):
    if request['method'] == 'GET':
       return requests.get(request['url'])

def extract_values(keep, json, vars):
    for k in keep:
        vars[k] = str(jsonpath.findall(keep[k], json)[0])

def main() -> None:

    with open('suite.yaml', 'r') as file:
        loaded_data = yaml.safe_load(file)
        global vars
        vars = loaded_data['vars']
        controllers = loaded_data['controllers']


    for controller in controllers:
        controller['request'] = replace_vars(controller['request'])

        response = send_request(controller['request'])
        
        extract_values(controller['keep'], response.json(), vars)

    print(vars)
