from typing import Optional, List
from pydantic import BaseModel

class InvoiceData(BaseModel):
    """
    Represents the internal data structure of an invoice.

    This includes financial details, metadata, line items, suppliers, and
    tax-related fields typically embedded in a full invoice object.
    """

    Currency: Optional[str]
    DateFormat: Optional[str]
    GLNatural: Optional[str]
    GLUnit: Optional[str]
    InvoiceDate: Optional[str]
    InvoiceNo: Optional[str]
    IsBillable: Optional[bool]
    IsCustom: Optional[bool]
    ListItem: Optional[list]
    ListSupplier: Optional[list]
    Name: Optional[str]
    Status: Optional[str]
    TaxCode: Optional[str]
    Total: Optional[float]
    TotalWithTax: Optional[float]
    UseDocAI: Optional[int]
    Tax1: Optional[float]
    Tax2: Optional[float]
    DueDate: Optional[str]
    approver: Optional[dict]

    class Config:
        extra = "allow"

class Invoice(BaseModel):
    """
    Represents a complete invoice object returned by the Xpens API.

    Includes metadata like status, timestamps, client linkage, and nested invoice data.
    """

    id: str
    status: str
    id_client: str
    invoice_data: InvoiceData
    user: Optional[dict]
    created_at: Optional[str]
    created_y_m: Optional[str]
    updated_at: Optional[str]
    insert_type: Optional[str]
    checksum: Optional[str]
    SageBatchNumber: Optional[int]
    status_details: Optional[str]
    rules_applied: Optional[bool]

    class Config:
        extra = "allow"