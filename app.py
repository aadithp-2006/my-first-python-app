from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Aadith!</h1><h2>My first OpenShift application is running successfully.</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
