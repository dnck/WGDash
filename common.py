import json
import datetime
import os
import yaml

SCRIPT_DIRNAME, SCRIPT_FILENAME = os.path.split(os.path.abspath(__file__))
PROJECT_ROOT_DIR = os.path.dirname(SCRIPT_DIRNAME)

def file_as_string(filepath):
    """
    Returns the yaml as a string
    """
    with open(filepath) as open_file:
        string_file = open_file.read()
    return string_file

def load_yaml_as_dict(filepath):
    """Load a yaml file as a python dictionary"""
    with open(filepath) as open_file:
        yaml_dict = yaml.safe_load(open_file)
    if yaml_dict:
        return yaml_dict
    return {}

def save_to_yaml(response, filepath, mode="w"):
    """
    Saves a yaml to file in a default 'w' mode
    """
    with open(filepath, mode) as fileobj:
        yaml.dump(response, fileobj)
