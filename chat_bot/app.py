import json
import os

import flask
from flask import request, send_from_directory

# <pre class="wp-block-code"><code># Flask app should start in global layout
app = flask.Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/favicon.png",
    )


@app.route("/")
@app.route("/home")
def home():
    return "Hello World"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    print(req)

    return {"fulfillmentText": "Hello from the bot world"}


if __name__ == "__main__":
    app.secret_key = "ItIsASecret"
    app.debug = True
    app.run()
