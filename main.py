from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here or use Replit Secrets
openai.api_key = os.getenv("https://www.bing.com/search?q=sk-proj-5-qat2az1i3qcy-xprkmkgxfapmlb_9ypvhth137fmhdb2l52m9ftscfoa671zenm9z-puiy70t3blbkfj-v-fauchje92sqjaeaergtpl5znlrxjis2dqo7wceygxr1wpysas_go0jfaxenljr_z17iycqa&gs_lcrp=EgRlZGdlKgcIBBBFGMIDMgcIABBFGMIDMgcIARBFGMIDMgcIAhBFGMIDMgcIAxBFGMIDMgcIBBBFGMIDMgcIBRBFGMIDMgcIBhBFGMIDMgcIBxBFGMID0gEJNzAwMTBqMGoxqAIIsAIB&FORM=ANNTA1&PC=U531")

@app.route("/", methods=["GET"])
def chat():
    user_input = request.args.get("txt")
    if not user_input:
        return jsonify({"text": "Missing 'txt' query parameter."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content
        return jsonify({"text": reply})
    except Exception as e:
        return jsonify({"text": f"Error: {str(e)}"}), 500

app.run(host="0.0.0.0", port=3000)
