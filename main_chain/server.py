from flask import Flask, render_template, jsonify, request

from main_chain.transactions.transactions_test import (
    generate_random_transactions,
    fetch_transactions,
    get_transactions_to_mine,
)

from main_chain.blockchain.blockchain import Blockchain

blockchain = Blockchain()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/see_transactions", methods=["GET"])
def see_transactions():
    transactions = fetch_transactions()
    return render_template("transactions.html", transactions=transactions)


@app.route("/see_chain")
def see_chain():
    print(blockchain.chain)
    return render_template(
        "blockchain.html", chain=blockchain.chain, miner_log=blockchain.miner_log
    )


@app.route("/api/make_transaction", methods=["POST"])
def make_transaction():
    generate_random_transactions()
    return "Done"


@app.route("/chain", methods=["GET"])
def get_chain():
    return jsonify(blockchain.chain), 200


@app.route("/mine", methods=["POST"])
def mine_block():
    data = request.get_json()
    transactions = data.get("transactions")
    miner_id = data.get("miner_id")

    if not transactions or not miner_id:
        return jsonify({"error": "Missing transactions or miner_id"}), 400

    blockchain.receive_mined_block(transactions, miner_id)
    return (
        jsonify({"message": "Block processed", "chain_length": len(blockchain.chain)}),
        200,
    )


@app.route("/fetch_transactions_to_mine", methods=["GET"])
def fetch_transactions_to_mine():
    txns = get_transactions_to_mine()
    return jsonify(txns), 200


@app.route("/log", methods=["GET"])
def get_log():
    return jsonify(blockchain.miner_log), 200


if __name__ == "__main__":
    app.run(debug=True)
