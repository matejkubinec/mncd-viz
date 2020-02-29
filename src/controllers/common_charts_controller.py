from flask import Blueprint, Response, jsonify, request
from drawing.barplot import draw_barplot
from drawing.treemap import draw_treemap
import json

common_charts = Blueprint("common_charts", __name__)


@common_charts.route("/api/common-charts/barplot", methods=["POST"])
def barplot():

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=402)

    valid = True
    errors = list()
    data = json.loads(request.data.decode("utf-8"))
    params = ["X", "Y", "labels", "xlabel", "ylabel"]

    for param in params:

        if param not in data:
            valid = False
            errors.append(f"Parameter '{param}' must not be none.")

    if not valid:
        response = {"errors": errors}
        return Response(jsonify(response), status=400)

    X = data["X"]
    Y = data["Y"]
    labels = data["labels"]
    xlabel = data["xlabel"]
    ylabel = data["ylabel"]

    svg = draw_barplot(X, Y, labels, xlabel, ylabel)
    return Response(svg, mimetype="image/svg+xml")


@common_charts.route("/api/common-charts/treemap", methods=["POST"])
def treemap():

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=402)

    valid = True
    errors = list()
    data = json.loads(request.data.decode("utf-8"))
    params = ["sizes", "label"]

    for param in params:

        if param not in data:
            valid = False
            errors.append(f"Parameter '{param}' must not be none.")

    if not valid:
        response = {"errors": errors}
        return Response(jsonify(response), status=400)

    sizes = data["sizes"]
    label = data["label"]

    svg = draw_treemap(sizes, label)
    return Response(svg, mimetype="image/svg+xml")
