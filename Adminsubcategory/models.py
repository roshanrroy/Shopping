from django.db import models

# Create your models here.

class SubcatModel(models.Model):
    subcat_id=models.AutoField(primary_key=True)
    cat_id = models.ForeignKey("AdminCategory.CategoryModel",db_column="cat_id",on_delete=models.CASCADE,default=None)
    subcategoryName=models.CharField(max_length=50)
    subcategoryImage = models.CharField(max_length=100)
    
    class Meta:
        db_table="tbl_subcategory"