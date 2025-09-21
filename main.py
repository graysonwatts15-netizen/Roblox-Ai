from flask import Flask, request, jsonify
from bardapi import BardCookies

app = Flask(__name__)
bard = BardCookies(cookie_dict={
    "__Secure-1PSID": "your_psid",
    "__Secure-1PSIDTS": "your_psidts",
    "__Secure-1PSIDCC": "your_psidcc"
})

@app.route("/", methods=["GET"])
def chat():
    txt = request.args.get("txt", "")
    response = bard.get_answer(txt)["content"]
    return jsonify({"text": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
