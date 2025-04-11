from typing import Optional, List, Union, Literal
from pydantic import BaseModel

class SortParam(BaseModel):
    """
    Represents a single sorting condition for an API query.

    Attributes:
        id (str): The field to sort by (e.g., 'created_at', 'status').
        order (str): Sort order, either 'asc' (ascending) or 'desc' (descending).
    """

    id: str
    order: Literal['asc', 'desc']

    def dict(self):
        """
        Convert the sorting query into a plain dictionary for serialization.

        :return: Dictionary representation, e.g., {'id': 'status', 'order': 'desc'}
        """
        return {"id": self.id, "order": self.order}


class FilterParam(BaseModel):
    """
    Represents a single filter condition for an API query.

    Attributes:
        id (str): The field to filter by (e.g., 'status', 'id').
        value (Union[str, int, bool, float]): The value to match.
    """

    id: str
    value: Union[str, int, bool, float]

    def dict(self):
        """
        Convert the filter query into a plain dictionary for serialization.

        :return: Dictionary representation, e.g., {'id': 'status', 'value': 'Completed'}
        """
        return {"id": self.id, "value": self.value}