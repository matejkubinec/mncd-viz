from flask import Blueprint, Response, jsonify, request
import json
import drawing.single_layer as sl
import drawing.single_layer_communities as slc

single_layer = Blueprint("single_user", __name__)


@single_layer.route("/api/single-layer/network", methods=["POST"])
def draw_network():

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
    svg = None

    if layout == "spring":
        svg = sl.spring_layout(edge_list)
    elif layout == "circular":
        svg = sl.circular_layout(edge_list)
    elif layout == "spiral":
        svg = sl.spiral_layout(edge_list)

    return Response(svg, mimetype="image/svg+xml")


@single_layer.route("/api/single-layer/community", methods=["POST"])
def draw_communities():

    if request.data is None:
        response = {"errors": ["Data cannot be none."]}
        return Response(jsonify(response), status=400)

    data = json.loads(request.data.decode("utf-8"))
    valid = True
    errors = list()

    params = ["edge_list", "comunity_list", "layout"]
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
    svg = None

    if layout == "spring":
        svg = slc.spring_layout_communities(edge_list, community_list)
    elif layout == "circular":
        svg = slc.circular_layout_communities(edge_list, community_list)
    elif layout == "spiral":
        svg = slc.spiral_layout_communities(edge_list, community_list)

    return Response(svg, mimetype="image/svg+xml")
