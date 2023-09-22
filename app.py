from flask import Flask,redirect,url_for,request,jsonify
from markupsafe import escape
import json, requests
from flask_cors import CORS
from flask_cors import cross_origin
import sys




app = Flask(__name__)



app.route('/IPgetter/', methods=["POST"])
def IP