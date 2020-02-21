from diagonal import diagonal
from flask import Flask, request, Response
app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to MNCD.Viz application!"


@app.route("/diagonal")
def diagonal_layout():

    if request.data is None or request.data == "":
        return Response("Data is required.")

    edgelist = request.data.decode("utf-8")
    svg = diagonal(edgelist)
    return Response(svg, mimetype="image/svg+xml")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
