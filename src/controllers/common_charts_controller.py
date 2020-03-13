from flask import Blueprint, Response, jsonify, request
from drawing.barplot import draw_barplot
from drawing.treemap import draw_treemap
import json

common_charts = Blueprint("common_charts", __name__)


@common_charts.route("/api/common-charts/barplot", methods=["POST"])
def barplot():
    """
    Create barplot

    swagger_from_file: specs/common_charts/barplot.yml
    """

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=402)

    valid = True
    errors = list()
    data = json.loads(request.data.decode("utf-8"))

    params = ["x", "y", "labels", "xlabel", "ylabel"]
    for param in params:

        if param not in data:
            valid = False
            errors.append(f"Parameter '{param}' must not be none.")

    if not valid:
        response = json.dumps({"errors": errors})
        return Response(response, status=400)

    X = data["x"]
    Y = data["y"]
    labels = data["labels"]
    xlabel = data["xlabel"]
    ylabel = data["ylabel"]
    params = data.get("params", {})
    image_format = "svg"

    if "image_format" in data:
        image_format = data["image_format"]

    img_data = draw_barplot(X, Y, labels, xlabel, ylabel, image_format, params)

    if image_format == "svg":
        return Response(img_data, mimetype="image/svg+xml")
    else:
        return Response(img_data, mimetype="image/png")


@common_charts.route("/api/common-charts/treemap", methods=["POST"])
def treemap():
    """
    Create treemap

    swagger_from_file: specs/common_charts/treemap.yml
    """

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
        response = json.dumps({"errors": errors})
        return Response(response, status=400)

    sizes = data["sizes"]
    label = data["label"]
    image_format = "svg"

    if "image_format" in data:
        image_format = data["image_format"]

    image_data = draw_treemap(sizes, label, image_format)

    if image_format == "svg":
        return Response(image_data, mimetype="image/svg+xml")
    else:
        return Response(image_data, mimetype="image/png")
