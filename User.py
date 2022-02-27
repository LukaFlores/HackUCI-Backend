import json
from flask import jsonify


class User:
    def __init__(self, age, name, gender, description, dateJoined, peopleSeen, userID):
        self.age = age
        self.name = name
        self.gender = gender
        self.description = description
        self.dateJoined = dateJoined
        self.peopleSeen = peopleSeen
        self.userID = userID

    @staticmethod
    def from_dict(source: dict):
        return User(source['age'], source['name'], source['gender'], source['description'], source['dateJoined'],
                    source['peopleSeen'], source['userID'])

    @staticmethod
    def from_json(source: json):
        return User.from_dict(json.load(source))  # convert JSON to dict then pass to the other method

    def to_dict(self):
        return {'age': self.age, 'name': self.name, 'gender': self.gender, 'description': self.description,
                'dateJoined': self.dateJoined, 'peopleSeen': self.peopleSeen, 'userID': self.userID}

    def to_json(self):
        return jsonify(self.to_dict())
