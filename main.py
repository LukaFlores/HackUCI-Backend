import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request, jsonify

from addUser import addUser
from getUser import getUser
from requestBuddies import requestBuddies
from getMatches import getMatches

cred = credentials.Certificate("hackuci2022-firebase-adminsdk-g1jrv-917eec5fe3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)


@app.route("/add", methods=["POST"])
def userInfo():
    return addUser(request.method, request.get_json(), db)


@app.route("/getUser", methods=["GET"])
def getTheUser():
    return jsonify(getUser(request.method, request.get_json(), db))


@app.route("/requestBuddies", methods=["POST"])
def getBuddies():
    return jsonify(requestBuddies(request.method, request.get_json(), db))


@app.route("/getMatches", methods=["GET"])
def findMatches():
    return jsonify(getMatches(request.method, request.get_json(), db))


if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0")
