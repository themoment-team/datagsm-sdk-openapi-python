"""Common response wrapper for DataGSM OpenAPI."""

from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class CommonApiResponse(BaseModel, Generic[T]):
    """공통 API 응답 래퍼 (Common API Response Wrapper).

    All API responses follow this structure with a data field containing
    the actual response payload.

    Attributes:
        status: Response status (e.g., "success", "error")
        code: HTTP status code
        message: Response message
        data: The actual response data of generic type T
    """

    status: str = Field(..., description="Response status")
    code: int = Field(..., description="HTTP status code")
    message: str = Field(..., description="Response message")
    data: Optional[T] = Field(None, description="Response data")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "success",
                "code": 200,
                "message": "Request successful",
                "data": {},
            }
        }
    )
