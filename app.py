from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Load quotes from JSON file
with open('quotes.json') as f:
    quotes = json.load(f)

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
