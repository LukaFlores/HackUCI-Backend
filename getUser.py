from User import User

def getUser(method, data, db):
    if method == "POST":
        user_id = data['ID']
        user_ref = db.collection("users").document(user_id)
        user_json = user_ref.get()
        return User(user_json)
        # return "<h1>Profile information for {} has been retrieved </h1>".format(data["Name"])
