from fastapi import APIRouter

from app.charts import multi_layer
from app.models import FigureResponse, SingleLayerCommunityBody, SingleLayerNetworkBody

router = APIRouter(prefix="/api/multi-layer", tags=["multi-layer"])


@router.post("/diagonal")
def diagonal():
    pass


@router.post("/hairball")
def hairball():
    pass


@router.post("slices")
def slices():
    pass


@router.post("slices-communities")
def slices_communities():
    pass
