import random
from datetime import datetime

from transactions.transactions import Transactions

transactions = Transactions()


def generate_random_transactions(num_transactions=20):
    print("here")
    transactions_list = []
    sender_ids = [f"user{i}" for i in range(1, 21)]  # Create 20 unique sender IDs
    receiver_ids = [
        f"user{random.randint(1, 21)}" for _ in range(num_transactions)
    ]  # Random receiver IDs
    amounts = [
        random.randint(1, 500) for _ in range(num_transactions)
    ]  # Random amounts from 1 to 500
    transaction_fees = [
        random.uniform(0.1, 5.0) for _ in range(num_transactions)
    ]  # Random fees from 0.1 to 5

    for i in range(num_transactions):
        transaction = {
            "senderid": random.choice(sender_ids),  # Random sender from the list
            "receiverid": receiver_ids[i],  # Random receiver
            "amt": amounts[i],  # Random amount
            "transaction_fee": round(
                transaction_fees[i], 2
            ),  # Random transaction fee rounded to 2 decimal places
            "timestamp": datetime.now().isoformat(),  # Current timestamp
        }
        transactions_list.append(transaction)
    transactions.add_transactions(transactions_list)
    return transactions_list


def fetch_transactions():
    return transactions.get_transactions()
