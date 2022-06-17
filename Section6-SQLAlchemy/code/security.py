from resources.user import User

# retrieve users by username
# username_mapping = {u.username: u for u in users}  # dict comprehension {key: value  for vars in sequence}
#
# # retrieve users by id
# userid_mapping = {u.id: u for u in users}


def Authenticate(username, password):
    # retrieve user object using find_by_username from User class
    user = User.find_by_username(username)  # default value set to None
    # compare user.password == password passing
    if user and user.password == password:
        return user
    # if user and user.password.__eq__(password): -> using __eq__ for string equals check
    # return user


def Identity(payload):
    # payload is the contents of the JWT Token
    user_id = payload['identity']
    return User.find_by_id(user_id)
