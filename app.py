from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:purple'>Hellooooooooo from python!!!</h1>"

if __name__ == "__main__":
    app.run(host='localhost')



