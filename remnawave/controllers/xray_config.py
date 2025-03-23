from typing import Annotated

from rapid_api_client.annotations import JsonBody

from remnawave.models import ConfigResponseDto
from remnawave.rapid import BaseController, get, post


class XrayConfigController(BaseController):
    @get("/xray/get-config", response_class=ConfigResponseDto)
    async def get_config(
        self,
    ) -> ConfigResponseDto:
        """Get Xray Config"""
        ...

    @post("/xray/update-config", response_class=ConfigResponseDto)
    async def update_config(
        self,
        body: Annotated[dict, JsonBody()],
    ) -> ConfigResponseDto:
        """Update Xray Config"""
        ...
