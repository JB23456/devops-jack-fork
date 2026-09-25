from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello, World! <a href="{url_for("contact")}">Contact</a>'


@app.route('/contact')
def contact():
    return "Contact me at C24522069@mytudublin.ie"


