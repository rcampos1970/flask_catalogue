# app.py

import json

with open('data.json') as f:
    data = json.load(f)

with open('new_file.json', 'w') as f:
    json.dump(data, f, indent=2)
    print("New json file is created from data.json file")