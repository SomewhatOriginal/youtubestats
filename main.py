from googleapiclient.discovery import build

api_key = "API KEY"

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(part='statistics', forUsername='MrBeast6000') 

response = request.execute()

print(response)

#So far only prints Mr. Beasts info...
