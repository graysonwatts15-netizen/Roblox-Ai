from flask import Flask, request, jsonify
from bardapi import Bard
import os

app = Flask(__name__)

# Use environment variables for security (recommended)
bard = Bard(cookie_dict={
    "__Secure-1PSID": os.getenv("BARD_PSID"),
    "__Secure-1PSIDTS": os.getenv("BARD_PSIDTS"),
    "__Secure-1PSIDCC": os.getenv("BARD_PSIDCC")
}, multi_cookies=True)

@app.route("/", methods=["GET"])
def chat():
    txt = request.args.get("txt", "")
    response = bard.get_answer(txt)["content"]
    return jsonify({"text": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
