import json

class User:
    def __init__(self, json):
        data = json.load()  # this will convert to dict
        self.age = data['age']
        self.name = data['name']
        self.gender = data['gender']
        self.description = data['description']
        self.dateJoined = data['dataJoined']
        self.peopleSeen = data['peopleSeen']
        self.userID = data['userID']

