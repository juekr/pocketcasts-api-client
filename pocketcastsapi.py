import requests

class PocketCastsAPI:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.login_url = "https://api.pocketcasts.com/user/login"
        self.client = requests.Session()
        self.ptoken = None
        self.api_headers = {
            'authority': 'api.pocketcasts.com',
            'accept': '*/*',
            'accept-language': 'de-DE,de;q=0.5',
            'authorization': '',
            'origin': 'https://play.pocketcasts.com',
            'referer': 'https://play.pocketcasts.com/',
            'sec-ch-ua': '"Brave";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

    def login(self):
        # Perform login and retrieve token
        credentials = {
            "email": self.email,
            "password": self.password,
            "scope": "webplayer"
        }
        res = self.client.post(self.login_url, headers=self.api_headers, data=credentials).json()
        self.ptoken = res["token"]
        self.api_headers['authorization'] = f'Bearer {self.ptoken}'

    def get_list_of_episodes(self):
        # Retrieve list of episodes from the API
        json_data = {}
        response = self.client.post('https://api.pocketcasts.com/user/history', headers=self.api_headers, json=json_data).json()
        return response["episodes"]

    def close_session(self):
        # Close the session
        self.client.close()
