from flask import Flask, render_template, request, jsonify, make_response
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    response = make_response(render_template("index.html"))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    api_key = data.pop("api_key", "AIzaSyBr0kL9tFoi6pnVBO9k1Pz9eqQyZSgJMsg")
        
    system_prompt = data.get("system", "") + "\\n\\nThe current date is March 18, 2026. Prioritize recent data up to 2026, do not artificially stop at 2023."
    user_prompt = data.get("messages", [{"content": ""}])[0]["content"]
    model_name = data.get("model", "gemini-2.5-flash")
    
    gemini_payload = {
        "systemInstruction": {
            "parts": [{"text": system_prompt}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_prompt}]
            }
        ],
        "tools": [
            {
                "googleSearch": {}
            }
        ],
        "generationConfig": {
            "maxOutputTokens": data.get("max_tokens", 4000)
        }
    }
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(
            url,
            headers=headers,
            json=gemini_payload,
            timeout=120
        )
        res_json = response.json()
        
        if response.status_code != 200:
            error_msg = res_json.get("error", {}).get("message", "Unknown error from Gemini API")
            return jsonify({"error": {"message": error_msg}}), response.status_code
            
        try:
            text_content = res_json["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            text_content = "Failed to parse response from Gemini: " + str(res_json)
        
        # Return in the format expected by the frontend code (Anthropic style)
        formatted_response = {
            "content": [{"type": "text", "text": text_content}]
        }
        return jsonify(formatted_response), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": {"message": str(e)}}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
