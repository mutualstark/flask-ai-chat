from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Store conversation history
conversation = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    global conversation

    data = request.get_json()
    user_message = data.get("message")

    conversation.append(f"User: {user_message}")

    # Combine conversation for context
    full_prompt = "\n".join(conversation) + "\nAI:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-coder:1.3b",
                "prompt": full_prompt,
                "stream": False
            }
        )

        ai_response = response.json()["response"].strip()

    except Exception as e:
        ai_response = f"Error connecting to Ollama: {str(e)}"

    conversation.append(f"AI: {ai_response}")

    return jsonify({"response": ai_response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
