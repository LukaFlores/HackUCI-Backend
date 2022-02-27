def getMatches(method, data, db):
    if method == "GET":
        APPUSER = data["ID"]
        potential_matches = db.collection("users").where(f"peopleSeen.{APPUSER}", "==", 'True').stream()
        matches = []
        for person in potential_matches:
            if person.to_dict()['peopleSeen'][APPUSER['name']] == 'True':
                matches.append(person)
        return matches
