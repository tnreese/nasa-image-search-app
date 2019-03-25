import urllib.request
import json
import webbrowser
     
from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('test.html')



@app.route('/', methods=['POST'])
def search():
    term = request.form['query']
    print(term)

    resultScreen(term)

    return render_template('secondpage.html')
	
	
def readAPI(searchTerm):
        # searchTerm = input("search:")
        apiurl = 'https://images-api.nasa.gov/search?q='+searchTerm
        print(apiurl)
        # call the api
        apiurlobj = urllib.request.urlopen(apiurl)
        # read JSON file
        apiread = apiurlobj.read()
        # convert JSON to Python so it is readable
        transapi = json.loads(apiread.decode('utf-8'))
        return(transapi)

#def getMetaData():
        #print(transapi['collection']['metadata'])
def resultScreen(term):
        transapi = readAPI(term)
        
        f= open("templates/secondpage.html","w", encoding="UTF8")
        
        metaData=0

        hitStr = "<p>Number of hits for {}: {} </p><hr></hr>".format(term, str( len(transapi['collection']['items'])))
        f.write(hitStr)
        
        for key in transapi['collection']['items']:
                if 'links' in key:
                        try:
                                if 'href' in key['links'][0]:
                                        f.write('<p>'+ key["data"][0]["title"]+ '</p>\n')

                                        f.write('<p><img src="'+ key["links"][0]["href"]+ '" alt=\"\" width=\"300\" height=\"168\" /></p>\n')

                                        f.write("<p>"+ key['data'][0]['description']+ "</p>\n<hr></hr>")

                                        metaData=metaData+1
                        except: 
                                print("missing data")

        f.close()
        
        return;




if __name__ == "__main__":
    app.run(debug=True)
	



    
