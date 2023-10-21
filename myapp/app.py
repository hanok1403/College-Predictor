from flask import Flask,render_template,request
from flask_wtf import CSRFProtect
from rank import rankCalculator


app=Flask(__name__)
app.secret_key = b'_53oi3uriq9pifpff;apl'
csrf=CSRFProtect(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/welcome",methods=["GET","POST"])
def welcome():
    if request.method == "POST":
        name=request.form["name"]
        rank=request.form["rank"]
        gender=request.form["gender"]
        course=request.form["course"]
        caste=request.form["caste"]
        rank=int(rank)
        caste=int(caste)
        l=rankCalculator(rank=rank,gender=gender,course=course,caste=caste)
        return render_template("welcome.html",l1=l,name=name)

    return 'ok'


