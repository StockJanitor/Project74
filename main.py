# Libraries importing
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Flask creation
flask_app = Flask(__name__)



# Loading home html
@flask_app.route("/")
def home():
    return render_template("index.html")


@flask_app.route("/PredictRegion", methods=["POST"])
def predict():
    # Grab requested values, convert to float
    float_features = [float(x) for x in request.form.values()]
    # Convert into list of np array
    features = [np.array(float_features)]
    # Run the model and predict outcome

    prediction = str(prediction[0])
    # load template and print out answer
    return render_template(
        "index.html",
        prediction_text="The Region of this house is {}.".format(prediction),
    )


if __name__ == "__main__":
    flask_app.run(debug=True)