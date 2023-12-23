import json

import requests
from config import DATA_FILENAME, ENDPOINT

with open(DATA_FILENAME, "r") as f:
    data = json.load(f)


def get_qa(topic, data):
    q = []
    a = []
    for d in data["data"]:
        if d["title"] == topic:
            for paragraph in d["paragraphs"]:
                for qa in paragraph["qas"]:
                    if not qa["is_impossible"]:
                        q.append(qa["question"])
                        a.append(qa["answers"][0]["text"])
            return q, a


questions, answers = get_qa(topic="Premier_League", data=data)

print("Number of available questions: {}".format(len(questions)))

json_data = {"questions": questions, "answers": answers}

response = requests.post(f"{ENDPOINT}/set_context", json=json_data)

print(response.json())
