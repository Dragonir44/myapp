from Data.users import users

def get_user_by_id(id):
    for user in users:
        if user["id"] == int(id):
            return user
    return None

def get_user_by_name(name):
    for user in users:
        if user["name"] == name:
            return user
    return None