import json

def read_data(filename=''):
    try:
        with open(filename) as f:
            readData = f.read()
            return json.dumps(readData)
    except FileNotFoundError:
        return {}

def write_data(data='', filename=''):
    with open(filename) as f:
        toJson = json.dumps(data)
        writeData = f.write(toJson)

def max_temperature(data='', data=''):
    
