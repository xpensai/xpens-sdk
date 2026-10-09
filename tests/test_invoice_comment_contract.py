"""Invoice update context and accounting values retain their wire contract."""
import unittest
from unittest.mock import Mock

from xpens.models.invoice import Invoice, InvoiceData
from xpens.services.invoice_service import InvoiceService


class InvoiceCommentContractTests(unittest.TestCase):
    def test_update_preserves_context_and_accounting_values(self):
        client = Mock()
        line = {'line_id': '507f1f77bcf86cd799439011', 'Comments': '  Expert name\n'}
        payload = {'comments': '  Narrative\n', 'ListItem': [line]}
        response = {key: None for key in Invoice.model_fields}
        nested = {key: None for key in InvoiceData.model_fields}
        response.update(id='507f1f77bcf86cd799439012', status='Completed', id_client='tenant',
                        status_details='Updated via API', invoice_data={**nested, **payload})
        client.request.return_value = response
        result = InvoiceService(client).update_invoice(response['id'], payload, comment='Updated via API')
        client.request.assert_called_once_with(method='PUT', path='/invoices/',
            params={'invoice_id': response['id'], 'comment': 'Updated via API'}, json=payload)
        self.assertEqual(result.status_details, 'Updated via API')
        returned = result.invoice_data.model_dump()
        for field, value in payload.items():
            self.assertEqual(returned[field], value)

    def test_default_update_context_remains_api_update(self):
        client = Mock()
        response = {key: None for key in Invoice.model_fields}
        response.update(id='invoice', status='Completed', id_client='tenant',
                        invoice_data={key: None for key in InvoiceData.model_fields})
        client.request.return_value = response
        InvoiceService(client).update_invoice('invoice', {})
        self.assertEqual(client.request.call_args.kwargs['params']['comment'], 'API UPDATE')
