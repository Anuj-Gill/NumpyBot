from flask import Flask, render_template, redirect, request
from bot import flan_t5_qa

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def userRequest():
  return render_template("home.html", title = "Request Page")

@app.route("/processRequest",methods = ["POST"])
def processReq():
  userRequest = request.form["request"]

  botResponse = flan_t5_qa(userRequest)

  return render_template("result.html", userRequest=userRequest, botResponse = botResponse["result"])


if __name__ == '__main__':
  app.run(debug=True)