from flask import Flask,redirect,url_for,request,jsonify, make_response
from markupsafe import escape
import json, requests
from flask_cors import CORS
from flask_cors import cross_origin
import sys




app = Flask(__name__)



app.route('/IPgetter/', methods=["POST"])
def ip_generator(): 
    data = request.json
    print("Data is: ", data, "\n\n")
    headers = request.headers
    print("Headers are: ", headers)

    return make_response(status= 200)



