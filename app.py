# Command to run the app is "flask run --debug" in terminal.
# Make sure to refresh your page if you don't see changes right away.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"