from django.db import models

# Create your models here.
class StatesModel(models.Model):
    state_id =models.AutoField(primary_key=True)
    statename = models.CharField(max_length=50)
  

    class Meta:
        db_table = "tbl_states"

class CityModel(models.Model):
    city_id =models.AutoField(primary_key=True)
    cityname = models.CharField(max_length=50)
    state_id=models.ForeignKey("StatesModel",db_column="state_id",on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = "tbl_city"
