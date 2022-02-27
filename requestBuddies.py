def requestBuddies(method, data, db):
    if method == "GET":
        user_id = data["ID"]
        APPUSER = db.collection("users").document(user_id).get().to_dict()
        users = db.collection("users").where(f"peopleSeen.{APPUSER}", "==", 'Null').limit(50).stream()
        return users
