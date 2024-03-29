import os
import json
import yaml


def read_file(filename):
    _, extension = os.path.splitext(filename)
    input_file = open(os.path.abspath(filename), 'r')

    if extension == '.json':
        return json.load(input_file)
    elif extension == '.yml' or extension == '.yaml':
        return yaml.safe_load(input_file)
