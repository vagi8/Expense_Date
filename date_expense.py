from flask import Flask
from flask import request
app = Flask(__name__)
import json

@app.route("/test")
def bye():
    return "Under Production"


if __name__ == '__main__':
    app.run(debug=True)
