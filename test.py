from pocketcastsapi import PocketCastsAPI
import config
import simplejson

pocketcasts_api = PocketCastsAPI(config.email, config.password)
pocketcasts_api.login()

json_history = pocketcasts_api.get_listening_history()
json_up_next = pocketcasts_api.get_up_next()
list_json_subscriptions = pocketcasts_api.get_subscriptions()
json_recommended = pocketcasts_api.get_recommended_episodes()

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

pocketcasts_api.close_session()
