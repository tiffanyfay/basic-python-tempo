from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def to_upper():
    data = request.get_json()
    text = data.get('text', '')
    return jsonify({"result": text.lower()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')