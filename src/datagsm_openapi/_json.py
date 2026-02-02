"""JSON serialization utilities for DataGSM OpenAPI SDK."""

from datetime import date, datetime
from typing import Any


def serialize_date(value: date) -> str:
    """Serialize a date to ISO format string.

    Args:
        value: Date object to serialize

    Returns:
        ISO format date string (YYYY-MM-DD)
    """
    return value.isoformat()


def serialize_datetime(value: datetime) -> str:
    """Serialize a datetime to ISO format string.

    Args:
        value: Datetime object to serialize

    Returns:
        ISO format datetime string
    """
    return value.isoformat()


def clean_params(params: dict[str, Any]) -> dict[str, Any]:
    """Clean query parameters by removing None values and serializing dates.

    Args:
        params: Dictionary of query parameters

    Returns:
        Cleaned dictionary with None values removed and dates serialized
    """
    cleaned: dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, datetime):
            cleaned[key] = serialize_datetime(value)
        elif isinstance(value, date):
            cleaned[key] = serialize_date(value)
        elif isinstance(value, bool):
            # Convert boolean to lowercase string for query params
            cleaned[key] = str(value).lower()
        else:
            cleaned[key] = value
    return cleaned
