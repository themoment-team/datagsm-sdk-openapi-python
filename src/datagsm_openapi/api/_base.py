"""Base API class for DataGSM OpenAPI SDK."""

from typing import Any, Optional, Type, TypeVar, cast

from pydantic import ValidationError

from .._http import HttpClient
from .._json import clean_params
from ..exceptions import ValidationException
from ..models import CommonApiResponse

T = TypeVar("T")


class BaseApi:
    """Base class for all API modules.

    Provides common functionality for making HTTP requests and parsing responses.
    """

    def __init__(self, http_client: HttpClient) -> None:
        """Initialize the base API.

        Args:
            http_client: HTTP client instance
        """
        self._http = http_client

    def _get(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
        response_type: Optional[Type[T]] = None,
    ) -> T:
        """Make a GET request and parse the response.

        Args:
            path: API endpoint path
            params: Query parameters
            response_type: Pydantic model class for response data

        Returns:
            Parsed response data

        Raises:
            ValidationException: If response validation fails
        """
        # Clean params (remove None values, serialize dates, etc.)
        clean = clean_params(params) if params else None

        # Make HTTP request
        response_data = self._http.get(path, params=clean)

        # If no response type specified, return raw data
        if response_type is None:
            return response_data  # type: ignore[return-value]

        # Parse as CommonApiResponse
        try:
            wrapped_response = CommonApiResponse[response_type].model_validate(  # type: ignore[valid-type]
                response_data
            )
            if wrapped_response.data is None:
                raise ValidationException(
                    message="Response data is None",
                    validation_errors=[],
                )
            return cast(T, wrapped_response.data)
        except ValidationError as e:
            raise ValidationException(
                message=f"Response validation failed: {e!s}",
                validation_errors=cast(list[dict[str, Any]], e.errors()),
            ) from e
