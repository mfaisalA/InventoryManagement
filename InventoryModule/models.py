from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

class Product(Item):
    brand_name = models.CharField(max_length=50, blank =True)


class Book(Item):
    publisher_name = models.CharField(max_length=100, blank =True)
    author_name = models.CharField(max_length=100)
    book_type = models.ForeignKey('BookType', on_delete=models.PROTECT)


class BookType(models.Model):
    name = models.CharField(max_length=100)

class Stock(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.PROTECT
        )
    expiry_date = models.DateField(null=True)
    qty_type = models.IntegerField(
        choices=[(1, "KG"), (2, "Ltr"), (3, "Piece"), (4, "Carton/Bundle")]
        )
    num_of_pieces = models.IntegerField(default=1)
    qty = models.IntegerField(default=0)
    min_qty = models.IntegerField(
        default=10,
        help_text = "Default is 10" )
    purchase_price = models.DecimalField(
        decimal_places=3,
        default=0,
        max_digits=11, 
        )
    selling_price = models.DecimalField(
        decimal_places=3,
        default=0,
        max_digits=11, 
        )

class InventoryLog(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.SET_NULL,
        null=True
    )
    update_type = models.IntegerField(
        choices = [(1, "Increased"),(2, "Decreased"),]
    )
    update_description = models.TextField()
    updated_by_type = models.IntegerField(
        choices = [(1, "Sales"),(2, "Purchase"),
        (3, "Sales Return"),(4, "By User"),]
    )
    # if updated by user his id else null
    updated_by = models.ForeignKey(
        CustomUser,
        on_delete = models.SET_NULL,
        null=True
    )
    updated_date = models.DateTimeField(auto_now=True)

    
    



