def requestBuddies(method, data, db):
    if method == "GET":
        APPUSER = data["ID"]
        users = db.collection("users").where("peopleSeen", "APPUSER", "==", False).stream().limit(50) + APPUSER
