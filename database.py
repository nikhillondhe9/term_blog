import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)


    """
    uri = "mongodb://127.0.0.1:27017"
    client = pymongo.MongoClient(uri)
    database = client['fullstack']
    collection = database['students']

    students = [student['name'] for student in collection.find()]

    print(students)
    """