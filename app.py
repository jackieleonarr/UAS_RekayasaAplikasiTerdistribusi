from flask import Flask, request,  jsonify
import json
import requests

app = Flask(__name__)

@app.route("/email", methods=["GET"])
def email():
    email = request.args.get('email')
    result = requests.get(f"https://api.eva.pingutil.com/email?email={email}")    
    return jsonify(json.loads(result.text))

@app.route("/word", methods=["GET"])
def word():
    email = request.args.get('content')
    result = requests.get(f"https://www.purgomalum.com/service/containsprofanity?text={email}")    
    return jsonify(json.loads(result.text))