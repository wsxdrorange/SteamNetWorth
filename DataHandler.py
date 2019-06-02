#Steam API KEY: B033C8D8105F6BED594C76462C7EDFB2
import requests

class DataHandler:
    def __init__(self, apiKey):
        self.apikey = apiKey
        self.baseURL = "https://api.steampowered.com"

    def getSteamID(self, input):
        vanityUrl = ""
        #if input is full link otherwise only username was inputted
        if "https://steamcommunity.com" in input:
            vanityUrl = input[input.rfind('/')+1:]
        else:
            vanityUrl = input

        requestURL = self.baseURL + "/ISteamUser/ResolveVanityURL/v1/?key=" + self.apikey + "&vanityurl=" + vanityUrl
        response = requests.get(requestURL)
        return response.json()["response"]["steamid"]

    def getInventoryNetWorth(self, user):
        response = requests.get()