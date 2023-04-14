from pocketcastsapi import PocketCastsAPI
from episodedb import EpisodesDB
import config

pocketcasts_api = PocketCastsAPI(config.email, config.password)
pocketcasts_api.login()
list_of_episodes = pocketcasts_api.get_list_of_episodes()

# Perform further operations with list_of_episodes as needed
edb = EpisodesDB('listen_history.db')
edb.insert_or_update_many_episodes(list_of_episodes)

print(edb.get_todownload_list(limit=15))

pocketcasts_api.close_session()
