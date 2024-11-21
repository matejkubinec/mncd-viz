from enum import Enum
import json
from typing import List, NamedTuple
from pydantic import BaseModel, field_validator, ValidationInfo, model_validator
from fastapi import Response, status
from matplotlib.figure import Figure
from app import figure


class ImageFormat(str, Enum):
    svg = "svg"
    png = "png"


class Layout(str, Enum):
    spring = "spring"
    circular = "circular"
    spiral = "spiral"


class Actor(NamedTuple):
    index: int
    name: str


class Layer(NamedTuple):
    index: int
    name: str


class Edge(NamedTuple):
    actor_from: int
    layer_from: int
    actor_to: int
    layer_to: int
    weight: int

    def to_list(self):
        return [
            self.actor_from,
            self.layer_from,
            self.actor_to,
            self.layer_to,
            self.weight,
        ]


class ActorToCommunity(NamedTuple):
    actor: int
    community: int


class Community(NamedTuple):
    index: int
    name: str


class FigureResponse(Response):
    def __init__(self, fig: Figure, format: ImageFormat):
        if format == ImageFormat.svg:
            content = figure.to_svg(fig)
            super().__init__(content, media_type="image/svg+xml")
        else:
            content = figure.to_png(fig)
            super().__init__(content, media_type="image/png")


class BarplotBody(BaseModel):
    image_format: ImageFormat = ImageFormat.svg
    x: List[int]
    xlabel: str
    y: List[int]
    ylabel: str
    labels: List[str]

    @model_validator(mode="after")
    def verify_lengths(self):
        if len(self.y) != len(self.x):
            raise ValueError("length of 'y' must match length of 'x'")

        if len(self.x) != len(self.labels):
            raise ValueError("length of 'labels' must match length of 'x'")

        return self


class TreemapBody(BaseModel):
    image_format: ImageFormat = ImageFormat.svg
    label: List[str]
    sizes: List[int]

    @model_validator(mode="after")
    def verify_lengths(self):
        if len(self.sizes) != len(self.label):
            raise ValueError("sizes length must match label length")
        return self

    @field_validator("sizes")
    def validate_sizes_total(cls, sizes: List[int], info: ValidationInfo):
        if sum(sizes) == 0:
            raise ValueError("sum of sizes must be greater than zero")
        return sizes


class SingleLayerNetworkBody(BaseModel):
    image_format: ImageFormat = ImageFormat.svg
    layout: Layout = Layout.circular
    edge_list: str


class SingleLayerCommunityBody(BaseModel):
    image_format: ImageFormat = ImageFormat.svg
    layout: Layout = Layout.circular
    edge_list: str
    community_list: str


class MultiLayerSlicesBody(BaseModel):
    image_format: ImageFormat = ImageFormat.svg
    edge_list: str


class MultiLayerCommunitySlicesBody(BaseModel):
    image_format: ImageFormat = ImageFormat.svg
    edge_list: str
    community_list: str


class NotImplementedResponse(Response):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            content=message,
        )
