#For the future https://www.youtube.com/watch?v=HrgckFxmFgU
#               https://www.youtube.com/watch?v=H4fQUHVvbX8

# Gets basicly import youtube? Also pip3 install youtube
# and setup a api key on console.developers.google.com
from apiclient.discovery import build

# Is what is searched up
search_term = "Minecraft"

#Api key
api_key = 'AIzaSyBMdLVOdV4QDsWe46unm5pQE0UBHadaGu4'




# "Opens" youtube
youtube = build('youtube','v3', developerKey=api_key)



#Searches youtube
# Or res could = youtube.search().list(q='minecraft',part='snippet',type='video',maxResults=50).execute()
req = youtube.search().list(q=search_term,part='snippet',type='video',maxResults=50)
res = req.execute()


#Lists seach terms
for item in res['items']:
    title = item['snippet']['title']
    print(item['snippet']['title'])

    with open('files.txt','a') as f:
        f.write('\n')
        f.write(item['snippet']['title'])




