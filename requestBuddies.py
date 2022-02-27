def requestBuddies(method, data, db):
    if method == "GET":
        APPUSER = data["ID"]
        users = db.collection("users").where(f"peopleSeen.{APPUSER}", "==", 'Null').limit(49).stream()
        users += db.collection("users").where("userID", "==", APPUSER).stream()
        for people in users:
            pass
        return users.to_dict()