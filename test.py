__author__ = 'viach_os'

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hallo, Zhuk!"

if __name__ == "__main__":
    app.run()