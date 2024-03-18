import json

from jsonhub.sdk.response.response import Response


class RawResponse(Response):

    def __init__(self,
                 status_code: int,
                 payload: dict,
                 ):
        total: int = payload.get('hydra:totalItems', 0)
        data: dict | list = payload.get('hydra:member', payload)
        super().__init__(json.dumps(data), status_code, total)
