import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Tech Connect!! - This is update#7 \n"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
