'''
Source:

Author: Raja CSP


'''
from flask import Flask,render_template
import random
import json

app  = Flask(__name__)
PORT = 3011


@app.route("/", methods=["GET","POST"])
def startpy():

    result = {
        "Greetings" : "P.S. I am here",
        "random_number" : random.randint(20, 100)
    }

    # return result

    return render_template("index.html", result = result)


if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
