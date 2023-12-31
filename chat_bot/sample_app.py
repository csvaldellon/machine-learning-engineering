from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, this is your Flask app!"


if __name__ == "__main__":
    app.run(debug=True)
