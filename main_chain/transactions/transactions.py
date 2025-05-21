from sortedcontainers import SortedSet


class Transactions:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Transactions, cls).__new__(cls)
            cls._instance.transactions = SortedSet(key=lambda x: -x[3])
        return cls._instance

    def add_transactions(self, transactions):
        for transaction in transactions:
            if all(
                k in transaction
                for k in (
                    "senderid",
                    "receiverid",
                    "amt",
                    "transaction_fee",
                    "timestamp",
                )
            ):
                transaction_tuple = (
                    transaction["senderid"],
                    transaction["receiverid"],
                    transaction["amt"],
                    transaction["transaction_fee"],
                    transaction["timestamp"],
                )
                self.transactions.add(transaction_tuple)
            else:
                raise ValueError(
                    f"Transaction {transaction} must contain senderid, receiverid, amt, transaction_fee, and timestamp"
                )

    def get_transactions(self):
        return [
            {
                "senderid": tx[0],
                "receiverid": tx[1],
                "amt": tx[2],
                "transaction_fee": tx[3],
                "timestamp": tx[4],
            }
            for tx in self.transactions
        ]

    def clear_transactions(self):
        self.transactions.clear()
