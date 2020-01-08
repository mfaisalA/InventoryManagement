from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import validate_email, validate_ipv4_address
from django.db import models
from InventoryModule.models import Stock, Category

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(
        'Supplier', 
        on_delete=models.PROTECT
        )
    invoice_ref_number = models.CharField(max_length=15,unique=True)
    stock_items = models.ManyToManyField(Stock)
    item_qty = models.IntegerField()
    total = models.DecimalField(
        decimal_places=3,
        default=0,
        max_digits=11
    )
    grand_total = models.DecimalField(
        decimal_places=3,
        default=0,
        max_digits=11
    )
    PAYMENT_CASH = "CSH"
    PAYMENT_CHEQUE = "CHQ"
    PAYMENT_CARD = "CRD"
    PAYMENT_CHOICES = (
        (PAYMENT_CASH, "Cash"),
        (PAYMENT_CHEQUE, "Cheque"),
        (PAYMENT_CARD, "Card"),
    )
    payment_type = models.CharField(
        max_length = 3,
        choices = PAYMENT_CHOICES
    )

    
    def __str__(self):
        return f'{self.invoice_ref_number}'


class Supplier(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    catogories = models.ManyToManyField(Category)
    contact = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)


