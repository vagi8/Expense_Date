from flask import Flask
#from flask_restful import reqparse, abort, Api, Resource
from flask_jsonpify import jsonify
from flask import request
app = Flask(__name__)
import json
import datefinder
import datetime
#api = Api(app)

@app.route("/find")
def train():
    inp=request.args['text']
    cat=request.args['cat']
    
    now = datetime.datetime.now()
    matches = list(datefinder.find_dates(inp,strict=True,base_date=now))
    matches.sort()
    
    if cat=='Flight' or cat=='flights' or cat=='Flights' or cat=='flight':
        try:
            ret=jsonify({'Invoice Date': str(matches[0].day) + '/'+ str(matches[0].month) + '/' + str(matches[0].year)})
        except:
            ret= jsonify({'Invoice Date': 0})
        return ret
    
    elif  (cat=='hotel') or (cat=='hotels') or (cat=='Hotel') or (cat=='Hotels'):
        try:
            i=len(matches) - 1
            ret=jsonify({'Invoice Date': str(matches[i].day) + '/'+ str(matches[i].month) + '/' + str(matches[i].year)})
        except:
            ret= jsonify({'Invoice Date': 0})
        return ret
    
    else:
        try:
            ret=jsonify({'Invoice Date': str(matches[0].day) + '/'+ str(matches[0].month) + '/' + str(matches[0].year)})
        except:
            ret= jsonify({'Invoice Date': 0})
        return ret

@app.route("/findweb")
def webfind():
    
    return "underproduction"
if __name__ == '__main__':
    app.run()