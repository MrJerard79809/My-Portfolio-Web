from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Hidden Formspree URL
FORMSPREE_ENDPOINT = "https://formspree.io/f/mnnvbjlv"

@app.route("/submit", methods=["POST"])
def handle_form():
    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "message": request.form["message"]
    }

    # Forward to Formspree (secret key hidden here)
    resp = requests.post(FORMSPREE_ENDPOINT, json=data, headers={"Content-Type": "application/json"})

    if resp.status_code == 200 or resp.status_code == 202:
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "fail"}), 400

if __name__ == "__main__":
    app.run(debug=True)
