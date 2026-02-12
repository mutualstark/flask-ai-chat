from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(_name_)

# Get API key from environment variable (Render)
OPENROUTER_API_KEY = os.getenv("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")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message")

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": user_message}
                ]
            }
        )

        result = response.json()

        if "choices" in result:
            ai_response = result["choices"][0]["message"]["content"]
        else:
            ai_response = "AI Error: Unable to get response."

    except Exception as e:
        ai_response = f"Error: {str(e)}"

    return jsonify({"response": ai_response})


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
