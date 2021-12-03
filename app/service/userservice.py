from . import mongo
from bson.json_util import dumps


def get_users():
    users = [doc for doc in mongo.db.users.find({})]

    print(users)
    return users


