def getMatches(method, data, db):
    if method == "GET":
        APPUSER = data["ID"]
        matches = db.collection("users").where(f"peopleSeen.{APPUSER}", "==", True).stream()
        return matches.to_dict()