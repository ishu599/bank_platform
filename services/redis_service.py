import redis
import json


class RedisService:

    def __init__(self):

        self.client = redis.Redis(

            host="redis",

            port=6379,

            decode_responses=True

        )

    def get(self, key):

        return self.client.get(key)

    def set(self, key, value, ttl=300):

        self.client.set(

            key,

            json.dumps(value),

            ex=ttl

        )

    def delete(self, key):

        self.client.delete(key)