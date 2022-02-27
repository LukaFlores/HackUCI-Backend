def requestBuddies(method, data, db):
    if method == "GET":
        APPUSER = data["ID"]
        users = db.collection("users").where(f"peopleSeen.{APPUSER}", "==", 'Null').limit(49).stream()

        return users.to_dict()