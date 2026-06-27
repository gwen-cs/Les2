from operator import truediv

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello/<string:name>')
def say_hello(name):
    return render_template("groet.html", firstname=escape(name), is_success=True)

