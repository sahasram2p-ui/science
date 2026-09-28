from flask import Flask, render_template, request, jsonify
from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL

app = Flask(__name__)
client = genai.Client(api_key=GEMINI_API_KEY)

COOKING_PROMPT = """
You are Cooking AI Assistant, a cooking and food-preparation information chatbot.

Answer ONLY questions related to cooking and food preparation, including
recipes, ingredients, cooking methods, baking, meal preparation, kitchen
techniques, food substitutions, spices, cookware, food storage, and general
culinary tips.

For food allergies, serious food-safety concerns, or medical dietary
conditions, give general safety guidance and advise consulting an appropriate
professional when needed.

If the user asks about software, programming, electronics, agriculture,
sports, movies, politics, or another topic unrelated to cooking or food
preparation, reply exactly:
"Sorry, I can answer only cooking and food-related questions."

Keep answers clear, practical, easy to follow, and beginner-friendly.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No data received."}), 400

        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"success": False, "error": "Please enter a message."}), 400

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=f"{COOKING_PROMPT}\n\nUser question:\n{user_message}"
        )

        return jsonify({"success": True, "reply": response.text})

    except Exception as e:
        print("ERROR:", repr(e))
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
