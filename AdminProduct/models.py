from django.db import models

# Create your models here.
from django.db import models

class ProductModel(models.Model):
    productId = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=255) 
    descriptions = models.TextField() 
    price = models.FloatField()
    sellPrice = models.FloatField()
    image1 = models.CharField(max_length=100,default=None)
    image2 = models.CharField(max_length=100,default=None)
    image3 = models.CharField(max_length=100,default=None)
    videoUrl = models.URLField(blank=True, null=True)  
    isActive = models.CharField(max_length=20) 
    subcat_id=models.ForeignKey("Adminsubcategory.SubcatModel",db_column="subcat_id",on_delete=models.CASCADE,default=None)

    class Meta:
        db_table ="tbl_product"