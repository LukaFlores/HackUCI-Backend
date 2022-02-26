import json

class User:
    def __init__(self, data: dict):
        self.age = data['age']
        self.name = data['name']
        self.gender = data['gender']
        self.description = data['description']
        self.dateJoined = data['dataJoined']
        self.peopleSeen = data['peopleSeen']
        self.userID = data['userID']

    @staticmethod
    def from_dict(source):
        pass