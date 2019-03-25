import urllib.request
import json
import webbrowser
     
#searchTerm = input("search:")
#apiurl = 'https://images-api.nasa.gov/search?q='+searchTerm
# call the api

#apiurlobj = urllib.request.urlopen(apiurl)
# read JSON file
#apiread = apiurlobj.read()
# convert JSON to Python so it is readable
#transapi = json.loads(apiread.decode('utf-8'))

#print (transapi['collection']['items'][0]['links'][0]['href'])
#thumbnail = (transapi['collection']['items'][0]['links'][0]['href'])
#webbrowser.open(picture)
#title = (transapi['collection']['items'][0]['data'][0]['title'])
#print (title)
def readAPI():
        searchTerm = input("search:")
        apiurl = 'https://images-api.nasa.gov/search?q='+searchTerm
        # call the api
        apiurlobj = urllib.request.urlopen(apiurl)
        # read JSON file
        apiread = apiurlobj.read()
        # convert JSON to Python so it is readable
        transapi = json.loads(apiread.decode('utf-8'))
        return(transapi)

#def getMetaData():
        #print(transapi['collection']['metadata'])
def resultScreen():
        transapi = readAPI()
        f= open("secondpage.html","w")
        metaData=0
        for key in transapi['collection']['items']:
                if 'links' in key:
                        try:
                                if 'href' in key['links'][0]:
                                        f.write('<p>'+ key["data"][0]["title"]+ '</p>\n')
                                        f.write('<p><img src="'+ key["links"][0]["href"]+ '" alt=\"\" width=\"300\" height=\"168\" /></p>\n')
                                        f.write("<p>"+ key['data'][0]['description']+ "</p>\n")
                                        metaData=metaData+1
                        except: 
                                print("missing data")
        f.close()
        
        return;

resultScreen()






    
