'''
SoftDev2 pd8
K 

'''

from flask import Flask, render_template
from util import 

app=Flask(__name__)


@app.route("/", methods=['GET','POST'])
def root():
    try:
        if request.form['name'] == "":
            return render_template("index.html", results = "You did not submit a query")
        #result = function
        else if not result:
            return render_template("index.html", results = "Your search did not yield any results")
        else:
            return render_template("index.html", results = result)
    except:
        return render_template("index.html", results = "")

if __name__ == "__main__":
    app.debug = True
    app.run()


