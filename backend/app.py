from flask import Flask, request, jsonify
from flask_cors import CORS
import ast
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# 🔥 Load AI Model for Code Completion
print("🔥 Loading AI Model...")
code_generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")
print("✅ Model Loaded Successfully!")

# ✅ AI Code Auto-Completion Route
@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.json
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        generated_code = code_generator(code, max_length=50, truncation=True)
        suggestion = generated_code[0]['generated_text']
        return jsonify({"suggestion": suggestion})
    except Exception as e:
        return jsonify({"error": f"Error generating code: {str(e)}"}), 500

# ✅ AI Code Error Detection Route
@app.route('/check_error', methods=['POST'])
def check_error():
    data = request.json
    code = data.get("code", "")

    if not code:
        return jsonify({"errors": "No code provided"}), 400

    try:
        ast.parse(code)  # Checks for syntax errors
        return jsonify({"errors": "No syntax errors detected."})
    except SyntaxError as e:
        error_message = f"Syntax Error on line {e.lineno}: {e.msg}"
        return jsonify({"errors": error_message})

# ✅ Run Flask Server
if __name__ == '__main__':
    app.run(debug=True)
