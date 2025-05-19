import os
from dotenv import load_dotenv
import redis

load_dotenv()


class RedisSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = redis.Redis.from_url(os.getenv("REDIS_URL"))
        return cls._instance
