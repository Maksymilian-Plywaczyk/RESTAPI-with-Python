from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}  # dict comprehension {key: value  for vars in sequence}

userid_mapping = {u.id: u for u in users}


def Authenticate(username, password):
    user = username_mapping.get(username, None)  # default value set to None
    if user and user.password == password:
        return user
    # if user and user.password.__eq__(password): -> using __eq__ for string equals check
    # return user


def Identity(payload):
    # payload is the contents of the JWT Token
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
