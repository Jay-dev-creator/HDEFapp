from django.db import models

# Create your models here.
class Items(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    cell_number = models.BigIntegerField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country_code = models.IntegerField(max_length=100, default='0700')
    item_name = models.CharField(max_length=100, null=True)
    item_type = models.CharField(max_length=100, null=True)

    item_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.id


