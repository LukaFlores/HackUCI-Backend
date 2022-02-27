def addUser(method,data,db):
    if method == "POST":
        set_empty = {'peopleSeen': []}
        for i in range(10):
            newUser = db.collection("users").document()
            newUser.set(set_empty)
        # WE CAN USE A DIFFERENT RETURN STATEMENT. JUST TO LET ME KNOW IT WAS WORKING
        return "<h1>Profile information for {} has been added </h1>"
