from pocketcastsapi import PocketCastsAPI
import config

def get_pocketcasts_api_client():
    return PocketCastsAPI(config.email, config.password)