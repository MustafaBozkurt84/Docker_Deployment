# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:20:14 2020

@author: mwolf
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route( "/" )
def welcome():
    return "Welcome All"

@app.route( "/predict" )
def predict_note_authentication():
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)


@app.route("/predict_file",methods=["POST"])
def prediction_file():
    def_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return "The predicted values for the csv is"+str(list(prediction))








if __name__=="__main__":
    app.run()
    