import json


class LoadFromjson:
    def load(self, path: str) -> dict:
        with open(path, "r") as file:
            return json.load(file)
