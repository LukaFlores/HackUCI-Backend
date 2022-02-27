def getUser(method, data, db):
    if method == "GET":
        user_id = data['ID']
        user_ref = db.collection("users").document(user_id)
        user_snap = user_ref.get()
        user_dict = user_snap.to_dict()
        return user_dict
