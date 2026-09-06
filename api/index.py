from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/compile", methods=["POST"])
def compile_code():
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "c")
    
    # Basic logic simulation for student debugging (e.g., checking common syntax issues)
    errors = []
    if language == "c" and "printf" in code and ";" not in code:
        errors.append("Syntax Error: Missing semicolon (;) at the end of a statement.")
    elif "int main" not in code and language == "c":
        errors.append("Structure Error: Missing 'int main()' function entry point.")
    
    if errors:
        return jsonify({
            "status": "failed",
            "errors": errors,
            "output": "Compilation failed due to syntax checks."
        })
    else:
        # Mock successful execution output
        return jsonify({
            "status": "success",
            "errors": [],
            "output": "Program compiled and executed successfully!\nOutput: Hello, Student!"
        })

if __name__ == "__main__":
    app.run(debug=True)
