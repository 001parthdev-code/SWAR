import json
import os 

class Storage:
    @staticmethod
    def save(filename,data):
        os.makedirs("data", exist_ok=True)

        with open(f"data/{filename}.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load(filename):
        path = f"data/{filename}.json"


        if not os.path.exists(path):
            return None

        with open(path, "r") as file:
            return json.load(file)