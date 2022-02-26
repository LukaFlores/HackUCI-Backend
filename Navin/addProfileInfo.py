


def addInfo(method,data,db):
    if method == "POST":
        newUser = db.collection("users").document()
        newUser.set(data)
        # WE CAN USE A DIFFERENT RETURN STATEMENT. JUST TO LET ME KNOW IT WAS WORKING
        return "<h1>Profile information for {} has been added </h1>".format(data["Name"])