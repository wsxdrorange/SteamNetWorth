from DataHandler import *

#Get input steam usernmae
name = "wsxdr50"
apiKey = "" #REPLACE WITH STEAM DEV API KEY
dataHandler = DataHandler(apiKey)

print(dataHandler.getSteamID(name))
