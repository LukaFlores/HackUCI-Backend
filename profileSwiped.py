'''
Created on Feb 26, 2022

@author: navin
'''

def swipeProfile(users,db):
    
    users = users.split(" ")
    if users[2]=="True":
        db.collection("users").document(users[0]).set({"peopleSeen":{users[1]:"True"}},
                                                      merge=True)
    return "<h1> User has been updated! <\h1>"

def checkMatch(users,db):
    users = users.split(" ")
    isUser2Matched = db.collection("users").document(users[0]).get().get("peopleSeen")[users[1]]
    isUser1Matched = db.collection("users").document(users[1]).get().get("peopleSeen")[users[0]]
    
    if isUser2Matched == "True" and isUser1Matched == "True":
        return "<h1> You have swiped right on each other!<\h1>"
    return "<h1> user2 has not seen or swiped on you <\h1>"