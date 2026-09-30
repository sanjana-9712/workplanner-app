from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "Put About page here!"

# ==================================== #
CORS(app) # This will enable CORS for all routes. Allows requests (to the API) from any origin (such as React frontend)
# ==================================== #

# /api/data route serves data to the frontend
@app.route('/api/data', methods=['GET'])
def get_data():
    print("api call for FETCH DATA!")
    data = {"message": "I am data"}
    return jsonify(data)

# /api/submit route receives data from the frontend
@app.route('/api/submit', methods=['POST'])
def submit_datax():
    print("api call for SUBMIT DATA!!!")
    payload = request.json
    print("Received:", payload)
    response = {"received": payload}
    return jsonify(response), 201

# ==================================== #
# Run the app on port 5000
# ==================================== #
if __name__ == '__main__':
    app.run()
    # * Running on http://127.0.0.1:5000