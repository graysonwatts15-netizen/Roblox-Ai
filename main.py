from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key (use Render environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def chat():
    user_input = request.args.get("txt", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response.choices[0].message.content
    return jsonify({"text": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
