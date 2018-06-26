import csv
import urllib.request
import json

with open("inputcsv.csv","r+") as infile,open("outputcsv.csv","w+") as outfile:
    inlist=csv.reader(infile)
    body={}
    for row in inlist:
        print (row)
        body["email"]=row[0]
        print (body)

        myurl = "https://api.fullcontact.com/v3/person.enrich"
        req = urllib.request.Request(myurl)
        req.add_header('Authorization', 'Bearer 8tutfGKG2cfNNYIdqYVeVsZdGCaDj0bc')
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)

        readed=json.loads(response.read())
        print (readed["fullName"])
        print (readed["linkedin"])

        newrow=row[0]+","+readed["fullName"]+","+readed["linkedin"]
        outfile.write(newrow)
        outfile.write("\n")

        

