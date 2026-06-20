import redis


class CacheService:

    def __init__(

        self

    ):

        self.client = redis.Redis(

            host="localhost",

            port=6379,

            decode_responses=True

        )

    def set(

        self,

        key,

        value,

        expiry=60

    ):

        self.client.setex(

            key,

            expiry,

            value

        )

    def get(

        self,

        key

    ):

        return self.client.get(

            key

        )

    def delete(

        self,

        key

    ):

        self.client.delete(

            key

        )