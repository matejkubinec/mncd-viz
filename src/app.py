import json
from diagonal import diagonal
from hairball import hairball_communities
from flask import Flask, request, Response
app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to MNCD.Viz application!"


@app.route("/multilayer/diagonal", methods=["POST"])
def diagonal_layout():

    if request.data is None or request.data == "":
        return Response("Data is required.")

    data = json.loads(request.data.decode("utf-8"))
    edgelist = data["edgelist"]
    svg = diagonal(edgelist)
    return Response(svg, mimetype="image/svg+xml")


@app.route("/multilayer/hairball/communities", methods=["POST"])
def hairball_plot_communities():
    if request.data is None or request.data == "":
        return Response("Data is required.")

    data = json.loads(request.data.decode("utf-8"))

    edgelist = data["edgelist"]

    if edgelist is None:
        return Response("EdgeList is required.", status=400)

    communities_list = data["communities"]

    if communities_list is None:
        return Response("Communities list is required.", status=400)

    svg = hairball_communities(edgelist, communities_list)

    return Response(svg, mimetype="image/svg+xml")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
