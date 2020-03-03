from flask import Blueprint, Response, jsonify, request
from drawing.multi_layer import diagonal_layout
from drawing.multi_layer_communities import hairball_layout
import json

multi_layer = Blueprint("multi_layer", __name__)


@multi_layer.route("/api/multi-layer/diagonal", methods=["POST"])
def draw_diagonal():
    """
    Multi Layer Diagonal Layout

    swagger_from_file: specs/multi_layer/diagonal.yml
    """

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=402)

    data = json.loads(request.data.decode("utf-8"))
    valid = True
    errors = list()

    params = ["edge_list"]
    for param in params:

        if param not in data:
            valid = False
            errors.append(f"Parameter '{param}' must not be none.")

    if not valid:
        response = json.dumps({"errors": errors})
        return Response(response, status=400)

    edge_list = data["edge_list"]
    image_format = "svg"

    if "image_format" in data:
        image_format = data["image_format"]

    image_data = diagonal_layout(edge_list, image_format)

    if image_format == "svg":
        return Response(image_data, mimetype="image/svg+xml")
    else:
        return Response(image_data, mimetype="image/png")


@multi_layer.route("/api/multi-layer/hairball", methods=["POST"])
def draw_hairball():
    """
    Multi Layer Hairball Layout

    swagger_from_file: specs/multi_layer/hairball.yml
    """

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=402)

    data = json.loads(request.data.decode("utf-8"))
    valid = True
    errors = list()

    params = ["edge_list", "community_list"]
    for param in params:

        if param not in data:
            valid = False
            errors.append(f"Parameter '{param}' must not be none.")

    if not valid:
        response = json.dumps({"errors": errors})
        return Response(response, status=400)

    edge_list = data["edge_list"]
    community_list = data["community_list"]
    image_format = "svg"

    if "image_format" in data:
        image_format = data["image_format"]

    image_data = hairball_layout(edge_list, community_list, image_format)

    if image_format == "svg":
        return Response(image_data, mimetype="image/svg+xml")
    else:
        return Response(image_data, mimetype="image/png")
