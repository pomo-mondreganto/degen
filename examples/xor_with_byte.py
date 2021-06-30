from models import DecodeRequest, DecodeResponse

BYTE = 137


def decode(req: DecodeRequest) -> DecodeResponse:
    resp = DecodeResponse(stream=req.stream, packets=req.packets)
    for packet in resp.packets:
        packet.content = bytes([x ^ BYTE for x in packet.content])
    return resp
