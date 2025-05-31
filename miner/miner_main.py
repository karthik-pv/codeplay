import time
import uuid
import requests
from main_chain.transactions.transactions import Transactions
from main_chain.blockchain.blockchain import Blockchain

transactions = Transactions()
blockchain = Blockchain()

miner_id = str(uuid.uuid4())

while True:
    try:
        transactions_list = requests.get(
            "http://localhost:5000/fetch_transactions_to_mine"
        ).json()
        print(transactions_list)
        if transactions_list:
            for transaction in transactions_list:
                print(f"Verifying transaction - {transaction}")
            requests.post(
                "http://localhost:5000/mine",
                json={"miner_id": miner_id, "transactions": transactions_list},
            )

        else:
            print("No transactions found.")
    except Exception as e:
        print(f"An error occurred while fetching transactions: {e}")

    time.sleep(10)
