from flask import Flask, jsonify, request, render_template
from project.utils import OxygenFlow
import config
import numpy as np

app = Flask(__name__)
@app.route("/")
def get_tested():
    return print("Home API is working")

@app.route("/OxygenFlow")
def get_oxygen_flow():
    data   = request.form
    age    = eval(data["age"])
    gender = data["gender"]
    spo2   = eval(data["spo2"])
    pr     = eval(data["pr"])
    cnc    = data["c/nc"]

    object = OxygenFlow(age,gender,spo2,pr,cnc)
    predic = object.get_oxygen_need()
    return jsonify({"result": f"The Needed Oxygen Flow for Patient is: {np.around(predic,2)}"})

if __name__ == "__main__":
    app.run(port=config.Port_Number)