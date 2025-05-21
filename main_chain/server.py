from flask import Flask, render_template

from transactions.transactions_test import (
    generate_random_transactions,
    fetch_transactions,
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/see_transactions", methods=["GET"])
def see_transactions():
    transactions = fetch_transactions()
    return render_template("transactions.html", transactions=transactions)


@app.route("/api/make_transaction", methods=["POST"])
def make_transaction():
    generate_random_transactions()
    return "Done"


if __name__ == "__main__":
    app.run(debug=True)
