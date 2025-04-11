# XPENS API

XPENS.AI provides a set of APIs for managing services such as invoices.

## Authentication Method

The API requires an API key to be included in the headers of each request:

```http
x-api-key: YOUR_API_KEY
```

### Example Request using cURL

```bash
curl -X GET "https://apis-dev.xpens.ai/integrations/invoices/?page=1&page_size=20" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

For support, contact: support@xpens.tech [support@xpens.tech](mailto:support@xpens.tech)



## Error Handling

| Status Code | Description                              |
|-------------|------------------------------------------|
| 401         | Unauthorized or missing API key          |
| 400         | Invalid API key format                   |
| 403         | Forbidden - insufficient permissions     |


## Documentation

Swagger documentation is available at:
[Xpens Swagger UI](https://apis-dev.xpens.ai/integrations/docs)

---

# XPENS Python SDK

For Python environments, the XPENS Python SDK is recommended for working with XPENS.AI APIs.


## Installation

```bash
pip install xpens-sdk  # or install from your repo path if not yet published
```
#### If sdk is not yet published, download the repository at:

```html
https://github.com/xpensai/xpens-sdk
```


## API Key and Base URL

Store the API key and base URL in your `.env` file:

```env
XPENS_API_KEY="__your_api_key__"
XPENS_API_URL="__your_base_url__"
```


## Instantiate the Xpens Client

### Using `.env` variables:

```python
from xpens import Xpens
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("XPENS_API_KEY")
base_url = os.getenv("XPENS_API_URL")

xp = Xpens(api_key=api_key, base_url=base_url)
```

### Using explicit variables:

```python
from xpens import Xpens

api_key = '__your_api_key__'
base_url = '__your_base_url__'

xp = Xpens(api_key=api_key, base_url=base_url)
```


## Usage

The `Xpens` object allows access to services like `invoices`. Below are some common use cases:

### List Invoices

```python
invoices = xp.invoices.list_invoices()
```

```python
from xpens.models import SortParam, FilterParam

sorting = [SortParam(id="created_at", order="desc")]
filters = [FilterParam(id="status", value="Completed")]

invoices = xp.invoices.list_invoices(
    page=1,
    page_size=5,
    sorting=sorting,
    filters=filters
)
```

### Get an Invoice by ID

```python
invoice = xp.invoices.get_invoice(
    invoice_id="67e590b7d32a143e271a3e6b"
)
```

### Create an Invoice

```python
with open("invoice.pdf", "rb") as file:
    response = xp.invoices.create_invoice(
        file_name="invoice.pdf",
        file_content=file,
        file_type="application/pdf"
    )
```

### Update an Invoice

```python
updated_fields = {
    "Currency": "USD"
}
updated = xp.invoices.update_invoice(
    invoice_id="__invoice_id__",
    data=updated_fields
)
```

### Delete an Invoice

```python
xp.invoices.delete_invoice(
    invoice_id="__invoice_id__"
)
```

---

## For XPENS Devs

For xpens devs to work on the sdk locally:

1. Clone the repository:
```
git clone https://github.com/xpensai/xpens-sdkcd xpens-python-sdk
```

2. Install dependencies and virtual environment:
````
python -m venv env
env/Scripts/activate
pip install .
````
3. Setup .env file:
```
XPENS_API_KEY=""
XPENS_API_URL=""
```

