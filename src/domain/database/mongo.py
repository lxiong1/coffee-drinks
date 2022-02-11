"""Access point to Mongo database"""

from pymongo import MongoClient


class Mongo:
    """Mongo database client"""

    HOST = "localhost"
    PORT = "27017"
    AUTH_SOURCE = "admin"
    USERNAME = "foo"
    PASSWORD = "bar"  # nosec

    def __init__(self):
        self.client = MongoClient(
            (
                f"mongodb://{self.USERNAME}:{self.PASSWORD}@"
                f"{self.HOST}:{self.PORT}/?authSource={self.AUTH_SOURCE}"
            )
        )
