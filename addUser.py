from faker import Faker
import numpy as np

fake = Faker()
def addUser(method, data, db):
    if method == "POST":
        g = ["Male", "Female", "Non-Binary", "other"]
        pwt = ["Morning", "Daytime", "Night", "No Preference"]
        pwl = ["Light", "Medium", "Intense", "No Preference"]
        pwr = ["One-Workout Stand", "Long time Relationship"]
        act = ["badminton", "baseball", "basketball", "dance", "football", "frisbee", "golf", "gym", "hiking", "hockey",
               "martial-arts", "running", "soccer", "softball", "swimming", "table-tennis", "tennis", "volleyball",
               "weights", "yoga", "other"]
        pa = [1/21, 1/21, 1/21, 1/21, 1/21, 1/21, 1/21, 1/21, 1/21, 1/21,
              1/21, 1/21, 1/21, 1/21, 1/21, 1/21, 1/21, 1/21,
              1/21, 1/21, 1/21]
        for _ in range(50):
            fdata = {
                'Full Name': fake.name(),
                'Birthday': fake.date(),
                'Gender': np.random.choice(g, p=[0.25, 0.25, 0.25, 0.25]),
                "Preferred Workout Time": np.random.choice(pwt, p=[0.25, 0.25, 0.25, 0.25]),
                "Preferred Workout Level": np.random.choice(pwl, p=[0.25, 0.25, 0.25, 0.25]),
                "Preferred Workout Relationship": np.random.choice(pwr, p=[0.5, 0.5]),
                "Activities": np.random.choice(act, p=pa)
            }
            newuser = db.collection("users").document()
            newuser.set(fdata)
        # WE CAN USE A DIFFERENT RETURN STATEMENT. JUST TO LET ME KNOW IT WAS WORKING
        return "<h1>Profile information for {} has been added </h1>"
