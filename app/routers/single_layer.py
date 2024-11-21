from fastapi import APIRouter

from app.charts import single_layer, single_layer_community
from app.models import FigureResponse, SingleLayerCommunityBody, SingleLayerNetworkBody

router = APIRouter(prefix="/api/single-layer", tags=["single-layer"])


@router.post("/network")
def network(body: SingleLayerNetworkBody):
    fig = single_layer.draw_network(body.edge_list, body.layout)
    return FigureResponse(fig, body.image_format)


@router.post("/community")
def community(body: SingleLayerCommunityBody):
    fig = single_layer_community.draw_communities(
        body.edge_list, body.community_list, body.layout
    )
    return FigureResponse(fig, body.image_format)
