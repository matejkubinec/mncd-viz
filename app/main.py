from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from app.routers import common_charts, single_layer, multi_layer

app = FastAPI(prefix="/api")

app.include_router(common_charts.router)
app.include_router(single_layer.router)
app.include_router(multi_layer.router)


@app.get("/")
async def root():
    return RedirectResponse("/docs", status_code=status.HTTP_302_FOUND)
