import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request, jsonify

from addProfileInfo import addInfo
from addUser import addUser

cred = credentials.Certificate("hackuci2022-firebase-adminsdk-g1jrv-61f7819fa4.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

app = Flask(__name__)
@app.route("/add", methods=["POST"])
def userInfo():
    addInfo(request.method,request.get_json(),db)


@app.route("/getUser", methods=["GET"])
def otherFunction():
    addUser(request.method,request.get_json(),db)



if __name__ == "__main__":
    app.run(threaded=True,host="0.0.0.0")