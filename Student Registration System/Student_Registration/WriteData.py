import os
import json
filename = "file.json"
def Write_data(data):
    with open(filename, "w") as file:
        json.dump(data,file, indent=4)