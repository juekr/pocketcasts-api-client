# pocketcasts-api-client

Python client for fetching listening history, subscriptions and recommended episodes. This is far from being officiall but as far as I know, the Pocketcasts dev are fine with people using their API. Please let me know if I am mistaken here.

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

## Installation

```bash
pip install git+https://github.com/juekr/pocketcasts-api-client.git
```

Then just import it like any other package: 

```python
from pocketcastsapi import get_pocketcasts_api
```

For now, there is one class and two functions that you can use:

- `PocketCastsAPI`
- `get_listening_history()`
- `get_recommended_episodes()`

## The PocketCastsAPI class

```python
from pocketcastsapi import PocketCastsAPI
import config

pocketcasts_api = PocketCastsAPI(config.email, config.password)
pocketcasts_api.login()

# ...

pocketcasts_api.close_session()
```

## get_listening_history

## get_recommended_episodes

## Example

You can test API access by inserting your login credentials into `config.py` (you can copy/rename `config-example.py` as a starting point) and use something like this:

```python
from pocketcastsapi import PocketCastsAPI
import config
import simplejson

pocketcasts_api = PocketCastsAPI(config.email, config.password)
pocketcasts_api.login()

json_history = pocketcasts_api.get_listening_history()
json_up_next = pocketcasts_api.get_up_next()
list_json_subscriptions = pocketcasts_api.get_subscriptions()
json_recommended = pocketcasts_api.get_recommended_episodes()
json_shownotes = pocketcasts_api.get_shownotes('7742e171-47ce-4a19-a68c-0a2be3522c7c')
json_full_info = pocketcasts_api.get_podcastinfo('913c2f40-f480-0134-ec5e-4114446340cb')

with open("pc_subscriptions.txt", "w") as file:
    file.write(simplejson.dumps(list_json_subscriptions[0], indent=4))

with open("pc_folders.txt", "w") as file:
    file.write(simplejson.dumps(list_json_subscriptions[1], indent=4))

with open("pc_recommended.txt", "w") as file:
    file.write(simplejson.dumps(json_recommended, indent=4))

with open("pc_history.txt", "w") as file:
    file.write(simplejson.dumps(json_history, indent=4))

with open("pc_up_next.txt", "w") as file:
    file.write(simplejson.dumps(json_up_next, indent=4))

with open("pc_shonotes.txt", "w") as file:
    file.write(simplejson.dumps(json_shownotes, indent=4))

with open("pc_fullinfo.txt", "w") as file:
    file.write(simplejson.dumps(json_full_info, indent=4))

pocketcasts_api.close_session()
```

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
