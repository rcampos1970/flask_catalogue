from flask import Flask
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    return "TCHAU"

if __name__ == "__main__":
    app.run()
