import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    # convert the data from json.
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    # extract the relevant information and use api and get the response and send it dialogflow.
    # helper function
    res = makeResponse(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# extract parameter values,  construct the resposne
def makeResponse(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    bank = parameters.get("bank-name")
    cost = {'Federal Bank': '6.70', 'Bandhan Bank': '8.5'}
    speech = "The interest rate is " + str(cost[bank])
    print("Response:")
    print(speech)
     return { "fulfillmentMessages": [ { "text": { "text": speech } }]}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    app.run(debug=True, port=port, host='0.0.0.0')
