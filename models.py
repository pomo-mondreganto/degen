import base64
from typing import Any

from pydantic import BaseModel, validator


class Packet(BaseModel):
    id: int
    capture_time: str
    content: bytes
    inbound: bool
    stream_id: int
    filter_data: int
    full_length: int

    @validator('content')
    def validate_content(cls, value: str):
        return base64.b64decode(value)

    def dict(self, **kwargs) -> dict[str, Any]:
        d = super(Packet, self).dict(**kwargs)
        d['content'] = base64.b64encode(d['content'])
        return d


class Stream(BaseModel):
    id: int
    source: str
    service_id: int
    endpoints: str
    filter_data: int
    total_size: int


class DecodeRequest(BaseModel):
    stream: Stream
    packets: list[Packet]


class DecodeResponse(BaseModel):
    stream: Stream
    packets: list[Packet]
