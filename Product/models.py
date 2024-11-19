from django.db import models
from django.contrib.auth.models import User  # Default User model

# Create your models here.
class CartModel(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,db_column="user_id", on_delete=models.CASCADE)
    productId = models.ForeignKey("AdminProduct.ProductModel",db_column="product_id", on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    
   

    class Meta:
        db_table = "tbl_cart"

    @property
    def total_price(self):
        """Calculate the total price for this cart item."""
        return self.qty * self.price


    
   
