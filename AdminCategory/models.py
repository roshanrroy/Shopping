from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    cat_id=models.AutoField(primary_key=True)
    categoryName=models.CharField(max_length=50)
    categoryImage = models.CharField(max_length=100,default=None)
    
    class Meta:
        db_table="tbl_category"