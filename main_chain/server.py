from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/api/make_transaction", methods=["POST"])
def make_transaction():
    return


if __name__ == "__main__":
    app.run(debug=True)
