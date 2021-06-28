import json

def process_cluener(resource):
    file_name = 'cluener.json'
    data = []
    with open('1.json') as f:
        for line in f:
            json_f = json.loads(line)
            data.append(json_f)
    for entry 