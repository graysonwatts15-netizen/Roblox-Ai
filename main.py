from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def chat():
    user_input = request.args.get("txt", "")
    if not user_input:
        return jsonify({"text": "No input provided."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content
        return jsonify({"text": reply})
    except Exception as e:
        return jsonify({"text": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
