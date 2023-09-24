from flask import Flask,redirect,url_for,request,jsonify, make_response
from markupsafe import escape
import json, requests
from flask_cors import CORS
from flask_cors import cross_origin
import sys
from werkzeug.middleware.proxy_fix import ProxyFix



app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)


@app.route('/IPgetter/', methods=["POST"])
def ip_generator(): 
    print(request)
    data = request.json
    print("Data is: ", data, "\n\n")
    headers = request.headers
    print("Headers are: ", headers)
    client_ip = request.remote_addr
    print("CLIENT IP: ", client_ip)

    print("ENVIRON: ", request.environ)
    return make_response("OK", 200)



if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True, port=5000)


