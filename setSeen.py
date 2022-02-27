'''
Created on Feb 26, 2022

@author: navin
'''


def setSeen(users,db): 
    users = users.split(" ")
    db.collection("users").document(users[0]).set({"peopleSeen":{users[1]:"False"}},merge=True)
    return "<h1> USER2 SEEN! <\h1>"

