import json
from redisController import RedisSingleton

redis = RedisSingleton()

TRANSACTIONS_REDIS_LIST = "transactions"


def add_transactions(transactions):
    for transaction in transactions:
        redis.rpush("transactions", json.dumps(transaction))
