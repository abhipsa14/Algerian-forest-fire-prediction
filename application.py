from flask import Flask,request,jsonify,render_template

# render_template for finding the html port
# jsonify getting data from website
# request for getting data from the client

import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

## import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/predictdata',methods=['POST','GET'])
## GET --> we are retrieving and POST ---> we are sending some data

def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        
    else:
        return render_template("home.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")