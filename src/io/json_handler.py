import json

def load_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def save_data(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
