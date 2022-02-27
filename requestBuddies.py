from flask import jsonify

def requestBuddies(method, data, db):
    if method == "POST":
        user_id = data["ID"]
        APPUSER = db.collection("users").document(user_id).get().to_dict()
        users = db.collection("users").limit(10).stream()

        set_dicts = []
        for person in users:
            print(person,'\n\n')
            person = person.to_dict()
            print(person)
            seen = person['peopleSeen']
            if user_id in seen:
                person['isLiked'][user_id] = 'isLiked'
            set_dicts.append(person)

        return set_dicts


        # 50 random users that are not in people seen
        # filter down to 10 best people
        # check in those peopleSeen for Luka's ID
        # if Luka ID is true possible match
        #       false possibility for non match
        # null can be equal to Luka swipes right and other user hasn't responded yet

        # values in people seen: "likedNotSeen", "notMatched", "matched"

        # Swipee gets "likedAndNotSeen

        # Andrew is appuser
        # get 50 people who andrew has not seen
        # filter to 10
        # those 10 people will be looped through
        #       check the people seen of the 10 selected:
        #           looking for andrew (only way is if "likedAndNotSeen")
        #           check people seen of Navin to look for andrew
        #               only update swipe right of a single user, not the other
        return users
