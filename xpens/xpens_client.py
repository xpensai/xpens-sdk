import requests
from .services import *
import logging
import json

class XpensClient:
    """
    Core SDK client for interacting with the Xpens API.

    Handles authentication, session configuration, and exposes resource-specific service modules.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initialize the client with authentication and base API URL.

        :param api_key: Your Xpens API key
        :param base_url: The root URL for the Xpens API
        """
        self.api_key = api_key
        self.base_url = base_url

        # Reuse a session for performance and connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": self.api_key,
            "accept": "application/json"  # Default header for all requests
        })

        # Initialize and expose services
        logging.info("Connected to Xpens API")
        self.invoices = InvoiceService(self)

    def request(self, method, path, params=None, json=None, files=None, headers=None):
        """
        Low-level request wrapper used by service modules to call API endpoints.

        :param method: HTTP method (GET, POST, PUT, DELETE, etc.)
        :param path: Endpoint path (relative to base_url)
        :param params: Optional URL query parameters
        :param json: Optional request body (JSON format)
        :param files: Optional file payload for multipart requests
        :param headers: Optional headers to override or add to the default ones
        :return: JSON-decoded response from the API
        :raises: requests.exceptions.HTTPError for HTTP-level errors
        """
        url = f"{self.base_url}{path}"
        headers = headers or {}
        headers["x-api-key"] = self.api_key  # Always ensure the key is present

        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=json,
                files=files,
                headers=headers
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            # Catch-all for unexpected errors
            logging.error(f"Unexpected error during request: {str(e)}")
            raise e