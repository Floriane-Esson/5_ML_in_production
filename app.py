from flask import Flask, request, jsonify, json, render_template
import joblib
import numpy
from typing import List
from sklearn.preprocessing import  StandardScaler
from werkzeug.exceptions import HTTPException

MODEL_PATH = "models/model.joblib"

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Return JSON instead of HTML for HTTP errors (which is the basic error
    response with Flask).
    """
    # Start with the correct headers and status code from the error
    response = e.get_response()
    # Replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

class MissingKeyError(HTTPException):
    # We can define our own error for the missing key
    code = 422
    name = "Missing key error"
    description = "JSON content missing key 'input'."

class MissingJSON(HTTPException):
    # We can define our own error for missing JSON
    code = 400
    name = "Missing JSON"
    description = "Missing JSON."

def make_prediction(input:List):
    # Load model 
    print("Load model")
    regressor = joblib.load(MODEL_PATH)
    print("...Done")

    prediction = regressor.predict(input)
    print(prediction)
    return prediction

@app.route("/predict", methods=["POST","GET"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        print("req")
        req = request.json
        print("req done") 
        print(req)
        if "input" not in req:
            raise MissingKeyError()
        quality = make_prediction(req["input"])
        response = {"Quality": str(quality)}
        return jsonify(response), 200
    raise MissingJSON

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)