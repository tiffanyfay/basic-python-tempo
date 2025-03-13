from flask import Flask, request, jsonify
import requests
import os
import logging
from opentelemetry import trace

# Acquire a tracer
tracer = trace.get_tracer("combined.tracer")

app = Flask(__name__)
logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(name)s:%(module)s:%(message)s', level=logging.INFO)

@app.route('/upper', methods=['POST'])
def upper():
    data = request.get_json()
    text = data.get('text', '')
    return to_upper(text)

@app.route('/lower', methods=['POST'])
def lower():
    data = request.get_json()
    text = data.get('text', '')
    return to_lower(text)

def to_upper(text):
    data = request.get_json()
    text = data.get('text', '')
    return jsonify({"result": text.lower()})

def to_upper(text: str):
    with tracer.start_as_current_span("to_upper") as span:
        span.set_attribute("text.length", len(text))
        result = text.upper()
        span.set_attribute("result.length", len(result))
        span.set_attribute("to_upper.value", result)
        return jsonify({"result": result})

# def to_lower(text):
#     data = request.get_json()
#     text = data.get('text', '')
#     return jsonify({"result": text.lower()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)