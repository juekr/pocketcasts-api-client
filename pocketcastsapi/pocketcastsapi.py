import requests

class PocketCastsAPI:
    def __init__(self):
        self.login_url = 'https://api.pocketcasts.com/user/login'
        self.recommended_episodes_url = 'https://api.pocketcasts.com/discover/recommend_episodes'
        self.listening_history_url = 'https://api.pocketcasts.com/user/history'
        self.subscriptions_url = 'https://api.pocketcasts.com/user/podcast/list'
        self.up_next_url = 'https://api.pocketcasts.com/up_next/list'
        self.shownotes_baseurl = 'https://cache.pocketcasts.com/episode/show_notes/'
        self.podcast_page_baseurl = 'https://play.pocketcasts.com/podcasts/'
        self.podcast_fullinfo_baseurl = 'https://podcast-api.pocketcasts.com/podcast/full/'
        self.podcast_starred_url = 'https://api.pocketcasts.com/user/starred'
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

    def login(self, email, password):
        # Perform login and retrieve token
        credentials = {
            "email": email,
            "password": password,
            "scope": "webplayer"
        }
        res = self.client.post(self.login_url, headers=self.api_headers, data=credentials).json()
        if "errorMessage" in res.keys():
            print(f'ERROR: {res["errorMessage"]}')
            return False
        self.ptoken = res["token"]
        self.api_headers['authorization'] = f'Bearer {self.ptoken}'
        return True

    def _call_api(self, url, response_keys = None, method='POST'):
        try:
            if method.lower() == "post":
                response = self.client.post(url, headers=self.api_headers).json()
            elif method.lower() == "get":
                response = self.client.get(url).json()
            else:
                print(f'Not a valid method: {method}')
                exit(1)
            if response_keys is None or response_keys == "":
                return response
            elif type(response_keys) == str:
                return response[response_keys]
            elif type(response_keys) == list and len(response_keys) == 1:
                return response[ response_keys[0] ]
            else:
                return [ response[elem] for elem in response_keys ]
        except Exception as e:
            print(f'ERROR while fetching {url} => {e}')
            return None

    def close_session(self):
        # Close the session
        self.client.close()

    def get_listening_history(self, limit = -1):
        # Retrieve list of episodes from the API
        result = self._call_api(self.listening_history_url, "episodes")
        return result[:limit] if limit > -1 else result

    def get_recommended_episodes(self, limit = 2):
        # Retrieve list of recommended episodes
        result = []
        while len(result) < limit and len(result) < 100:
            result += self._call_api(self.recommended_episodes_url, "episodes")
        return result[:limit]

    def get_up_next(self):
        # Retrieve list of recommended episodes
        return self._call_api(self.up_next_url, "episodes")

    def get_subscriptions(self):
        # Retrieve a list of podcasts that you've subscribed to
        return self._call_api(self.subscriptions_url, [ "podcasts", "folders" ])

    def get_podcast_page(self, podcast_uuid):
        # Retrieve podcast details
        return f'{self.podcast_page_baseurl}{podcast_uuid}'

    def get_shownotes(self, episode_uuid):
        # Retrieve shownotes for an episode uuid
        return self._call_api(f'{self.shownotes_baseurl}{episode_uuid}', method='GET', response_keys=['show_notes'])

    def get_podcastinfo(self, podcast_uuid):
        # Retrieve all infos on a podcast
        return self._call_api(f'{self.podcast_fullinfo_baseurl}{podcast_uuid}', method='GET', response_keys=None)


def get_listening_history(email, password, limit = -1) -> list:
    """Fetches a user's listening history via Pocketcast's api

    Args:
        email (_type_): authentication email
        password (_type_): authentication password
        limit (int, optional): number of results to return – defaults to -1 (= all; currently API returns a maximum of 100)

    Returns:
        list: [JSON] list of podcast episodes
    """
    api = PocketCastsAPI()
    if api.login(email, password) == True:
        result = api.get_listening_history(limit)
        api.close_session()
        return result
    else:
        api.close_session()
        return []

def get_recommended_episodes(email, password, limit = 2) -> list:
    """Fetches recommendations for a user via Pocketcast's api

    Args:
        email (_type_): authentication email
        password (_type_): authentication password
        limit (int, optional): number of results to return – defaults to 2 (= all; currently the maximum is 100)

    Returns:
        list: [JSON] list of podcast episodes
    """
    api = PocketCastsAPI()
    if api.login(email, password) == True:
        result = api.get_recommended_episodes(limit)
        api.close_session()
        return result
    else:
        api.close_session()
        return []