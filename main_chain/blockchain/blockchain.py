import time
import hashlib

from main_chain.transactions.transactions import Transactions


class Blockchain:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Blockchain, cls).__new__(cls)
            cls._instance.chain = []
            cls._instance.miner_log = []
            cls._instance.verified_transactions = set()
            cls._instance.create_genesis_block()
        return cls._instance

    def create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "transactions": [],
            "previous_hash": "0",
            "nonce": 0,
        }
        genesis_block["hash"] = self.calculate_hash(genesis_block)
        self.chain.append(genesis_block)

    def calculate_hash(self, block):
        block_string = f"{block['index']}{block['timestamp']}{block['transactions']}{block['previous_hash']}{block['nonce']}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def receive_mined_block(self, transactions, miner_id):
        tx_tuples = [
            (
                tx["senderid"],
                tx["receiverid"],
                tx["amt"],
                tx["transaction_fee"],
                tx["timestamp"],
            )
            for tx in transactions
        ]
        new_tx = [tx for tx in tx_tuples if tx not in self.verified_transactions]
        if len(new_tx) >= 3:
            new_block = {
                "index": len(self.chain),
                "timestamp": time.time(),
                "transactions": tx_tuples,
                "previous_hash": self.chain[-1]["hash"],
                "nonce": 0,
            }
            new_block["hash"] = self.calculate_hash(new_block)
            self.chain.append(new_block)
            self.verified_transactions.update(tx_tuples)
            self.miner_log.append(
                {
                    "miner": miner_id,
                    "status": "accepted",
                    "block_index": new_block["index"],
                }
            )
        else:
            unverified = [
                tx for tx in tx_tuples if tx not in self.verified_transactions
            ]
            tx_module = Transactions()
            tx_module.add_transactions(
                [
                    {
                        "senderid": tx[0],
                        "receiverid": tx[1],
                        "amt": tx[2],
                        "transaction_fee": tx[3],
                        "timestamp": tx[4],
                    }
                    for tx in unverified
                ]
            )
            self.verified_transactions.update(tx_tuples)
            self.miner_log.append({"miner": miner_id, "status": "rejected"})
