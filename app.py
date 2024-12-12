from flask import Flask, render_template,escape,request,redirect,url_for
from urlShortener import shorten_url,retrive_url_from_key

app = Flask(__name__)

# home page for url shortening
@app.route("/home",methods= ['POST','GET'])
def hello_world():
    short_u = None
    if request.method == "POST":
        url = request.form["url"]
        result = shorten_url(url)
        short_u = result

    return render_template('index.html', short_u=short_u)

# actual url page
@app.route("/<key>")
def get_org_url(key):
    org = retrive_url_from_key(key)
    return redirect(org)




