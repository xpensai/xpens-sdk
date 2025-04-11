import logging
from requests.exceptions import HTTPError

import json
from typing import Optional, List
from ..models.invoice import Invoice, InvoiceData
from ..models.query import SortParam, FilterParam

# Default sorting criteria for invoices
DEFAULT_SORTING = [SortParam(id="created_at", order="desc")]
DEFAULT_FILTERS = []

class InvoiceService:
    """
    A service class to interact with the Xpens Invoice API.
    Provides methods to list, fetch, create, update, and delete invoices.
    """

    def __init__(self, client):
        """
        Initialize the service with a given XpensClient instance.

        :param client: An instance of the API client to perform requests
        """
        self.client = client
        self.base_path = "/invoices"

    def list_invoices(
        self,
        page: int = 1,
        page_size: int = 20,
        sorting: List[SortParam] = None,
        filters: List[FilterParam] = None
    ) -> List[Invoice]:
        """
        Retrieve a paginated list of invoices with optional sorting and filters.

        :param page: Page number for pagination
        :param page_size: Number of results per page
        :param sorting: Optional list of sorting criteria
        :param filters: Optional list of filter conditions
        :return: A list of Invoice model instances
        """
        method = "GET"
        path = f"{self.base_path}/"
        params = {
            "page": page,
            "page_size": page_size,
            "sorting": json.dumps([sort.dict() for sort in (sorting or DEFAULT_SORTING)]),
            "filters": json.dumps([filter.dict() for filter in (filters or DEFAULT_FILTERS)]),
        }

        response = self.client.request(method=method, path=path, params=params)
        invoice_list = [Invoice(**item) for item in response.get("items", [])]
        return invoice_list

    def get_invoice(self, invoice_id: str) -> Invoice:
        """
        Retrieve a single invoice by its ID.

        :param invoice_id: The unique ID of the invoice
        :return: An Invoice model instance
        """
        method = "GET"
        path = f"{self.base_path}/"
        params = {
            "filters": json.dumps([{"id": "id", "value": invoice_id}]),
        }

        response = self.client.request(method=method, path=path, params=params)
        invoice = Invoice(**response.get("items", [])[0])
        return invoice

    def create_invoice(self, file_name, file_content, file_type="application/pdf"):
        """
        Create a new invoice by uploading a file.

        :param file_name: Name of the file being uploaded
        :param file_content: File object (opened in binary mode)
        :param file_type: MIME type of the file (default: application/pdf)
        :return: Response from the API
        """
        method = "POST"
        path = f"{self.base_path}/"
        files = {
            "file": (file_name, file_content, file_type)
        }
        response = self.client.request(method=method, path=path, files=files)
        return response

    def delete_invoice(self, invoice_id: str):
        """
        Delete an invoice by ID.

        :param invoice_id: The ID of the invoice to delete
        :return: Response from the API
        """
        method = "DELETE"
        path = f"{self.base_path}/"
        params = {"invoice_id": invoice_id}

        response = self.client.request(method=method, path=path, params=params)
        return response

    def update_invoice(self, invoice_id: str, data: dict, comment: str = "API UPDATE") -> Invoice:
        """
        Update an existing invoice by ID with new data.

        :param invoice_id: The ID of the invoice to update
        :param data: A dictionary representing the updated invoice fields
        :param comment: Optional comment for update context (default: 'API UPDATE')
        :return: Updated Invoice model instance
        """
        method = "PUT"
        path = f"{self.base_path}/"
        params = {
            "invoice_id": invoice_id,
            "comment": comment,
        }

        response = self.client.request(method=method, path=path, params=params, json=data)
        invoice = Invoice(**response)
        return invoice

    def validate_invoice(self, invoice_id: str):
        """
                Validate an existing

                :param invoice_id: The ID of the invoice to validate
                """
        method = "PUT"
        path = f"{self.base_path}/validate"
        params = {
            "invoice_id": invoice_id
        }

        response = self.client.request(method=method, path=path, params=params)
        return response


"""
    Not yet implemented
    
    def export_invoices(self, invoice_ids: list[str]):
        method = "POST"
        path = f"{self.base_path}/export"

        return self.client.request(method=method, path=path, json=invoice_ids)

"""




