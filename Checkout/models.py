from django.db import models
from django.contrib.auth.models import User

class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,db_column="user_id", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city_id = models.ForeignKey("Location.CityModel",db_column="City_id", on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)  
    status = models.CharField(max_length=20, default='pending') 
    orderdatetime = models.DateTimeField()
    finaltotal = models.FloatField(default=None)

    class Meta:
        db_table ="tbl_order"
