from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateUserRequestDto,
    DeleteUserResponseDto,
    EmailUserResponseDto,
    TelegramUserResponseDto,
    UpdateUserRequestDto,
    UserResponseDto,
    UsersResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class UsersController(BaseController):
    @post("/users", response_class=UserResponseDto)
    async def create_user(
        self,
        body: Annotated[CreateUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Create User"""
        ...

    @post("/users/update", response_class=UserResponseDto)
    async def update_user(
        self,
        body: Annotated[UpdateUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Update User"""
        ...

    @get("/users/v2", response_class=UsersResponseDto)
    async def get_all_users_v2(
        self,
    ) -> UsersResponseDto:
        """Get All Users"""
        ...

    @patch("/users/revoke/{uuid}", response_class=UserResponseDto)
    async def revoke_user_subscription(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Revoke User Subscription"""
        ...

    @patch("/users/disable/{uuid}", response_class=UserResponseDto)
    async def disable_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Disable User"""
        ...

    @delete("/users/delete/{uuid}", response_class=DeleteUserResponseDto)
    async def delete_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> DeleteUserResponseDto:
        """Delete User"""
        ...

    @patch("/users/enable/{uuid}", response_class=UserResponseDto)
    async def enable_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Enable User"""
        ...

    @patch("/users/reset-traffic/{uuid}", response_class=UserResponseDto)
    async def reset_user_traffic(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Reset User Traffic"""
        ...

    @get("/users/short-uuid/{short_uuid}", response_class=UserResponseDto)
    async def get_user_by_short_uuid(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the user")],
    ) -> UserResponseDto:
        """Get User By Short UUID"""
        ...

    @get("/users/sub-uuid/{subscription_uuid}", response_class=UserResponseDto)
    async def get_user_by_subscription_uuid(
        self,
        subscription_uuid: Annotated[str, Path(description="UUID of the subscription")],
    ) -> UserResponseDto:
        """Get User By Subscription UUID"""
        ...

    @get("/users/uuid/{uuid}", response_class=UserResponseDto)
    async def get_user_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Get User By UUID"""
        ...

    @get("/users/username/{username}", response_class=UserResponseDto)
    async def get_user_by_username(
        self,
        username: Annotated[str, Path(description="Username of the user")],
    ) -> UserResponseDto:
        """Get User By Username"""
        ...

    @get(
        "/users/tg/{telegram_id}",
        response_class=TelegramUserResponseDto,
    )
    async def get_users_by_telegram_id(
        self,
        telegram_id: Annotated[str, Path(description="Telegram ID of the user")],
    ) -> TelegramUserResponseDto:
        """Get Users By Telegram ID"""
        ...

    @get("/users/email/{email}", response_class=EmailUserResponseDto)
    async def get_users_by_email(
        self,
        email: Annotated[str, Path(description="Email of the user")],
    ) -> EmailUserResponseDto:
        """Get Users By Email"""
        ...
