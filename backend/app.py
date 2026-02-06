from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import json
from groq import Groq
from flask_cors import CORS

from prompts import prepare_prompt

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY missing in .env")

# Setup Groq client
client = Groq(api_key=GROQ_API_KEY)

# Fast + good quality model (free tier friendly)
MODEL_NAME = "openai/gpt-oss-120b"
# You can also use: "mixtral-8x7b-32768"

app = Flask(__name__)
CORS(app)

# Load menu data
with open("menu_data.json", "r", encoding="utf-8") as f:
    MENU_DATA = json.load(f)


def ask_ai(prompt):
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful restaurant assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    user_question = data.get("query")
    diet_mode = data.get("diet", "all")

    if not user_question:
        return jsonify({"error": "Question is required"}), 400

    prompt = prepare_prompt(MENU_DATA, user_question, diet_mode)
    answer = ask_ai(prompt)

    return jsonify({
        "question": user_question,
        "diet_mode": diet_mode,
        "answer": answer
    })


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Restaurant FAQ backend running (Groq)",
        "model": MODEL_NAME
    })


if __name__ == "__main__":
    app.run(debug=True)
