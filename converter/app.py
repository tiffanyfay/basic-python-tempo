from flask import Flask, request, jsonify
from opentelemetry import trace
import requests
import os

app = Flask(__name__)

@app.route('/upper', methods=['POST'])
def to_upper():
    data = request.get_json()
    text = data.get('text', '')
    
    url = os.environ.get('UPPER_URL')
    if not url:
        return jsonify({"error": "UPPER_URL not configured"}), 500
        
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json={"text": text}, headers=headers)
    
    if response.status_code != 200:
        return jsonify({"error": "Upstream service error"}), response.status_code
        
    return jsonify(response.json())

@app.route('/lower', methods=['POST'])
def to_lower():
    data = request.get_json()
    text = data.get('text', '')
    
    url = os.environ.get('LOWER_URL')
    if not url:
        return jsonify({"error": "LOWER_URL not configured"}), 500
        
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json={"text": text}, headers=headers)
    
    if response.status_code != 200:
        return jsonify({"error": "Upstream service error"}), response.status_code
        
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0')