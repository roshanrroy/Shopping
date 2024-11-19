from django.db import models

class ItemModel(models.Model):
    item_id =models.AutoField(primary_key=True)
    order_id=models.ForeignKey("Checkout.OrderModel",db_column="order_id",on_delete=models.CASCADE)
    productId=models.ForeignKey("AdminProduct.ProductModel",db_column="productId",on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    price = models.FloatField()

    class Meta:
        db_table = "tbl_item"