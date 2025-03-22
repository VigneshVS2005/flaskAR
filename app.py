from flask import Flask, request, jsonify, send_file
import openai

app = Flask(__name__)

# Prompt Refiner for Enhanced Responses
def refine_prompt(original_prompt):
    refined_prompt = f"Enhanced: {original_prompt} with more context for better Copilot results."
    return refined_prompt

# Route to refine prompts
@app.route('/refine/<prompt>', methods=['GET'])
def get_refined_prompt(prompt):
    refined = refine_prompt(prompt)
    return jsonify({"original_prompt": prompt, "refined_prompt": refined})

# Route to improve KQL queries
@app.route('/optimize_kql/<query>', methods=['GET'])
def optimize_kql(query):
    optimized_query = query.replace("*", "specific_column")  # Example logic
    return jsonify({"original_query": query, "optimized_query": optimized_query})

# ➕ New Route to Serve the YAML File
@app.route('/file/<fileName>', methods=['GET'])
def get_file(fileName):
    try:
        return send_file(f"./{fileName}", download_name=fileName, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Railway's $PORT, or default to 5000
    app.run(host='0.0.0.0', port=port)
    
