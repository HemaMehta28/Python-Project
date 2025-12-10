import os
import json
filename = "file.json"
def Read_data():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
            if content:
                return json.loads(content)
    return []