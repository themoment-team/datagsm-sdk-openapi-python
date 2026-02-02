"""NEIS API module for DataGSM OpenAPI SDK."""

from dataclasses import dataclass
from datetime import date as Date
from typing import Optional

from ..models import Meal, Schedule
from ._base import BaseApi


@dataclass
class MealRequest:
    """급식 조회 요청 파라미터 (Meal Query Parameters).

    Use either 'date' for a single day or 'from_date' and 'to_date' for a date range.

    Attributes:
        date: Single date to query
        from_date: Start date for range query
        to_date: End date for range query
    """

    date: Optional[Date] = None
    from_date: Optional[Date] = None
    to_date: Optional[Date] = None

    def to_params(self) -> dict[str, Optional[object]]:
        """Convert to query parameters dictionary.

        Returns:
            Dictionary of query parameters
        """
        params: dict[str, Optional[object]] = {
            "date": self.date,
            "fromDate": self.from_date,
            "toDate": self.to_date,
        }
        return params


@dataclass
class ScheduleRequest:
    """학사일정 조회 요청 파라미터 (Schedule Query Parameters).

    Use either 'date' for a single day or 'from_date' and 'to_date' for a date range.

    Attributes:
        date: Single date to query
        from_date: Start date for range query
        to_date: End date for range query
    """

    date: Optional[Date] = None
    from_date: Optional[Date] = None
    to_date: Optional[Date] = None

    def to_params(self) -> dict[str, Optional[object]]:
        """Convert to query parameters dictionary.

        Returns:
            Dictionary of query parameters
        """
        params: dict[str, Optional[object]] = {
            "date": self.date,
            "fromDate": self.from_date,
            "toDate": self.to_date,
        }
        return params


class NeisApi(BaseApi):
    """NEIS 데이터 API (NEIS Data API).

    Provides methods for querying school meal and schedule information from NEIS.
    """

    def get_meals(self, request: Optional[MealRequest] = None) -> list[Meal]:
        """급식 정보 조회 (Get Meal Information).

        Query school meal information for a specific date or date range.

        Args:
            request: Query parameters (optional, defaults to today)

        Returns:
            List of meals

        Example:
            >>> from datetime import date
            >>> api = NeisApi(http_client)
            >>>
            >>> # Get today's meals
            >>> today_meals = api.get_meals()
            >>>
            >>> # Get meals for a specific date
            >>> request = MealRequest(date=date(2026, 2, 3))
            >>> meals = api.get_meals(request)
            >>>
            >>> # Get meals for a date range
            >>> request = MealRequest(
            ...     from_date=date(2026, 2, 1),
            ...     to_date=date(2026, 2, 7)
            ... )
            >>> week_meals = api.get_meals(request)
        """
        req = request or MealRequest(date=Date.today())
        return self._get("/v1/neis/meals", params=req.to_params(), response_type=list[Meal])

    def get_schedules(self, request: Optional[ScheduleRequest] = None) -> list[Schedule]:
        """학사일정 정보 조회 (Get Schedule Information).

        Query school schedule/event information for a specific date or date range.

        Args:
            request: Query parameters (optional, defaults to today)

        Returns:
            List of schedules

        Example:
            >>> from datetime import date
            >>> api = NeisApi(http_client)
            >>>
            >>> # Get today's schedules
            >>> today_events = api.get_schedules()
            >>>
            >>> # Get schedules for a specific date
            >>> request = ScheduleRequest(date=date(2026, 3, 1))
            >>> schedules = api.get_schedules(request)
            >>>
            >>> # Get schedules for a date range
            >>> request = ScheduleRequest(
            ...     from_date=date(2026, 3, 1),
            ...     to_date=date(2026, 3, 31)
            ... )
            >>> month_schedules = api.get_schedules(request)
        """
        req = request or ScheduleRequest(date=Date.today())
        return self._get(
            "/v1/neis/schedules", params=req.to_params(), response_type=list[Schedule]
        )
