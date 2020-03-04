from flask import Blueprint, Response, jsonify, request
import json
import drawing.single_layer as sl
import drawing.single_layer_communities as slc

single_layer = Blueprint("single_user", __name__)


@single_layer.route("/api/single-layer/network", methods=["POST"])
def draw_network():
    """
    Single Layer Network

    swagger_from_file: specs/single_layer/network.yml
    """

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=402)

    data = json.loads(request.data.decode("utf-8"))
    params = ["edge_list", "layout"]
    valid = True
    errors = list()

    for param in params:

        if param not in data:
            valid = False
            errors.append("Parameter 'edge_list' must not be none.")

    if not valid:
        response = json.dumps({"errors": errors})
        return Response(response, status=400)

    layout = data["layout"]
    edge_list = data["edge_list"]
    image_format = "svg"

    if "image_format" in data:
        image_format = data["image_format"]

    image_data = None
    if layout == "spring":
        image_data = sl.spring_layout(edge_list, image_format)
    elif layout == "circular":
        image_data = sl.circular_layout(edge_list, image_format)
    elif layout == "spiral":
        image_data = sl.spiral_layout(edge_list, image_format)

    if image_format == "svg":
        return Response(image_data, mimetype="image/svg+xml")
    else:
        return Response(image_data, mimetype="image/png")


@single_layer.route("/api/single-layer/community", methods=["POST"])
def draw_communities():
    """
    Single Layer Network

    swagger_from_file: specs/single_layer/communities.yml
    """

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=400)

    data = json.loads(request.data.decode("utf-8"))
    valid = True
    errors = list()

    params = ["edge_list", "community_list", "layout"]
    for param in params:

        if param not in data:
            valid = False
            errors.append(f"Parameter '{param}' must not be none.")

    if not valid:
        response = json.dumps({"errors": errors})
        return Response(response, status=400)

    layout = data["layout"]
    edge_list = data["edge_list"]
    community_list = data["community_list"]
    image_format = "svg"

    if "image_format" in data:
        image_format = data["image_format"]

    image_data = None
    if layout == "spring":
        image_data = slc.spring_layout_communities(
            edge_list,
            community_list,
            image_format
        )
    elif layout == "circular":
        image_data = slc.circular_layout_communities(
            edge_list,
            community_list,
            image_format
        )
    elif layout == "spiral":
        image_data = slc.spiral_layout_communities(
            edge_list,
            community_list,
            image_format
        )

    if image_format == "svg":
        return Response(image_data, mimetype="image/svg+xml")
    else:
        return Response(image_data, mimetype="image/png")
