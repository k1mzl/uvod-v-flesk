from flask import Flask, render_template , request
import random
#pip install flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/calclove",methods=["POST"])
def calclove():

    d= request.form
    ime1 = d.get("ime1").lower()
    ime2 = d.get("ime2").lower()
    if len(str(ime1)) or len(str(ime2)) <= 0:
        rez = "0%"
        
        
    if ime1== "kim" or ime2== "kim":
        rez = f"{random.randint(90,100)}%"
        return render_template("index.html",rezultat=rez)
    

    rez = f"{ime1} + {ime2} = {random.randint(0,100)}%"
    return render_template("index.html",rezultat=rez)

app.run(debug = True)
