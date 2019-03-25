import urllib.request
import json
import webbrowser
     
searchTerm = input("search:")
apiurl = 'https://images-api.nasa.gov/search?q='+searchTerm
# call the api

apiurlobj = urllib.request.urlopen(apiurl)
# read JSON file
apiread = apiurlobj.read()
# convert JSON to Python so it is readable
transapi = json.loads(apiread.decode('utf-8'))

#print (transapi['collection']['items'][0]['links'][0]['href'])
#thumbnail = (transapi['collection']['items'][0]['links'][0]['href'])
#webbrowser.open(picture)
#title = (transapi['collection']['items'][0]['data'][0]['title'])
#print (title)
def readAPI(url):
        # call the api
        apiurlobj = urllib.request.urlopen(url)
        # read JSON file
        apiread = apiurlobj.read()
        # convert JSON to Python so it is readable
        transapi = json.loads(apiread.decode('utf-8'))
        return(transapi)

def getMetaData():
        print(transapi['collection']['metadata'])
def resultScreen():
        getMetaData()
        for key in transapi['collection']['items']:
                if 'href' in key['links'][0]:
                        print(key['data'][0]['title'])
                        webbrowser.open(key['links'][0]['href'])
                        print(key['data'][0]['description'])
        return;
resultScreen()
pictureLink = transapi['collection']['items'][0]['href']
pictureList = readAPI(pictureLink)
smallPicture = pictureList[3]
print (smallPicture)




    
