import json

def get_weather(location: str) -> str:
    # This function is a placeholder for a real weather API
    return "The weather in {} is 72 degrees and sunny.".format(location)


tools_message = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather...",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
        },
    }
]


class Tools:
    def __init__(self):
        self.mapping = {"get_weather": get_weather}

    def call(self, message: dict, callback=None):
        tool_name = message["name"]
        parameters = message.get("parameters", {})
        call_id = message["call_id"]

        output = self.mapping[tool_name](**parameters)
        if callback:
            callback(json.dump(output), call_id)