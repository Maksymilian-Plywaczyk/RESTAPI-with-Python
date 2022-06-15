class User:
    def __init__(self, _id, username, password):
        # using _id because id is a Python Keyword and we don't want to use that as a variable name
        self.id = _id
        self.username = username
        self.password = password
