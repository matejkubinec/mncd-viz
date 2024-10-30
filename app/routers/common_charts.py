from app.models import BarplotBody, FigureResponse, TreemapBody
from app.charts import common
from fastapi import APIRouter

router = APIRouter(prefix="/api/common-charts", tags=["common-charts"])


@router.post("/barplot")
async def barplot(body: BarplotBody):
    fig = common.draw_barplot(body.labels, body.x, body.xlabel, body.y, body.ylabel)
    return FigureResponse(fig, body.image_format)


@router.post("/treemap")
async def treemap(body: TreemapBody):
    fig = common.draw_treemap(body.label, body.sizes)
    return FigureResponse(fig, body.image_format)
