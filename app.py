from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello going to make contribution in open source</p>"

if __name__=="__main__":
    app.run(debug=True)