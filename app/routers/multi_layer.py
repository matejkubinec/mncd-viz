from fastapi import APIRouter

from app.charts import multi_layer, multi_layer_community
from app.models import (
    FigureResponse,
    MultiLayerCommunitySlicesBody,
    MultiLayerSlicesBody,
    NotImplementedResponse,
)

router = APIRouter(prefix="/api/multi-layer", tags=["multi-layer"])


@router.post("/diagonal", include_in_schema=False)
def diagonal():
    return NotImplementedResponse("Multi-layer diagonal chart is not implemented yet.")


@router.post("/hairball", include_in_schema=False)
def hairball():
    return NotImplementedResponse("Multi-layer hairball chart is not implemented yet.")


@router.post("/slices")
def slices(body: MultiLayerSlicesBody):
    fig = multi_layer.draw_slices(body.edge_list)
    return FigureResponse(fig, body.image_format)


@router.post("/slices-communities")
def slices_communities(body: MultiLayerCommunitySlicesBody):
    fig = multi_layer_community.draw_slices_with_communities(
        body.edge_list,
        body.community_list,
    )
    return FigureResponse(fig, body.image_format)
