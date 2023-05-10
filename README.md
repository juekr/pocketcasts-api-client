# pocketcasts-api-client

Python client for fetching listening history, subscriptions and recommended episodes. This is far from being officiall but as far as I know, the Pocketcasts dev are fine with people using their API. Please let me know if I am mistaken here.

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

## Installation

```bash
pip install git+https://github.com/juekr/pocketcasts-api-client.git
```

Then just import it like any other package:

```python
from pocketcastsapi import PocketCastsAPI # if you want to interface the API class directly (for coomplexer queries)
from pocketcastsapi import get_listening_history
from pocketcastsapi import get_recommended_episodes
from pocketcastsapi import get_starred_episodes
```

For now, there is one class and three functions that you can use:

- `PocketCastsAPI`
- `get_listening_history()`
- `get_recommended_episodes()`
- `get_starred_episodes()`

## The PocketCastsAPI class

I recommend putting your login credentials in a separate file `config.py` (you can copy/rename `config-example.py` as a starting point). Then just `import config.py` and use `config.email` and `config.password` wherever needed.

Here's an example:

```python
from pocketcastsapi import PocketCastsAPI
import config

pocketcasts_api = PocketCastsAPI()
pocketcasts_api.login(email=config.email, password=config.password)

# ... do stuff, documentation to be added, here a few examples:
shownotes = pocketcasts_api.get_shownotes('7742e171-47ce-4a19-a68c-0a2be3522c7c')
podcast_info = pocketcasts_api.get_podcastinfo('913c2f40-f480-0134-ec5e-4114446340cb')
subscriptions = pocketcasts_api.get_subscriptions()

for rec in pocketcasts_api.get_recommended_episodes(limit = 10):
    print(pocketcasts_api.get_shownotes(rec['uuid'])) # full shownotes don't come by default

for sub in pocketcasts_api.get_subscriptions()[0]: # [0] is for subscriptions, [1] for folders
    print(pocketcasts_api.get_podcastinfo(sub["uuid"]))

pocketcasts_api.close_session()
```

## Functions to use without the PocketCastsAPI class

When using the functions without the `PocketCastsAPI` class, you need to provide the login credentials as parameters. Some functions also have a `limit` parameter for limiting the output (and at least in one case limiting the number of API calls made in the background); in aller other cases `-1` means "all".

### get_listening_history(email, password, limit = -1, historyfile = None) -> list

Retrieves the listening history of a logged in user.

The problem: There are no timestamps or dates being provided. So the listening history is just an unordered
list of episodes you've listened to some time in the past.

If a `historyfile` is provided – and that really only makes sense, if you call the API regularly –, then
the list is saved the first time (along with the current date), and on each subsequent call it checks whether an
episode is already in the list or is a new addition to be saved with the then current date. So if you call the API,
let's say, once a day, you over time get a daily log of podcast eisodes you've listened to.

The API only delivers 100 results (even when using `-1` as `limit`), but it can be more if the `historyfile` is being used.

The function makes an extra call to retrieve the shownotes for each episode returned. If that is not what you want,
you can use the `PocketCastsAPI` class to fetch the listening history.

### get_recommended_episodes()

The function makes an extra call to retrieve the shownotes for each episode returned. If that is not what you want,
you can use the `PocketCastsAPI` class to fetch the listening history.

### get_starred_episodes()

The function makes an extra call to retrieve the shownotes for each episode returned. If that is not what you want,
you can use the `PocketCastsAPI` class to fetch the listening history.

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
