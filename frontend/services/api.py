import requests

BASE_URL = "http://localhost:8000"


class API:

    @staticmethod
    def classify_inbox():

        response = requests.post(f"{BASE_URL}/classify/inbox")

        response.raise_for_status()

        return response.json()

    @staticmethod
    def history():

        response = requests.get(f"{BASE_URL}/history")

        response.raise_for_status()

        return response.json()

    @staticmethod
    def stats():

        response = requests.get(f"{BASE_URL}/stats")

        response.raise_for_status()

        return response.json()
