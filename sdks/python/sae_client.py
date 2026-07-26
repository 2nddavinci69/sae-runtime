import requests

class SAEClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def verify_vitt_token(self, token: str):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(f"{self.base_url}/vitt/verify", json={"token": token}, headers=headers)
        return response.json()
