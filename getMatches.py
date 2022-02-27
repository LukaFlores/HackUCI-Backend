def getMatches(method, data, db):
    if method == "GET":
        APPUSER = data["ID"]
        matches = db.collection("users").where(f"peopleSeen.{APPUSER}", "==", 'True').limit(10).stream()
        return matches.to_dict()
