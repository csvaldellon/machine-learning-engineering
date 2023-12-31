import requests
from config import HOSTED_ENDPOINT, LOCAL_ENDPOINT

new_questions = [
    "How many teams compete in the Premier League ?",
    "When does the Premier League starts and finishes ?",
    "Who has the highest number of goals in the Premier League ?",
]

json_data = {
    "questions": new_questions,
}


def test_get_answer(endpoint):
    response = requests.post(f"{endpoint}/get_answer", json=json_data)
    for d in response.json():
        print("\n".join(["{} : {}".format(k, v) for k, v in d.items()]) + "\n")


if __name__ == "__main__":
    endpoint = input("Endpoint [local or hosted]")
    if endpoint == "local":
        test_get_answer(LOCAL_ENDPOINT)
    elif endpoint == "hosted":
        test_get_answer(HOSTED_ENDPOINT)
    else:
        print("Wrong endpoint.")
