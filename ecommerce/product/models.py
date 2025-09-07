from django.db import models

# Create your models here.
class Product(models.Model):
   product_title = models.CharField(max_length=300)
   usage_id = models.ForeignKey('Usage', on_delete=models.CASCADE)
   gender_id = models.ForeignKey('Gender', on_delete=models.CASCADE)
   category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
   subcategory_id = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
   product_type_id = models.ForeignKey('ProductType', on_delete=models.CASCADE)
   img_url = models.URLField(max_length=500)

# Usage model
class Usage(models.Model):
    name = models.CharField(max_length=100)

# Gender model
class Gender(models.Model):
    name = models.CharField(max_length=50)

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

# SubCategory model
class SubCategory(models.Model):
    name = models.CharField(max_length=100)

# ProductType model
class ProductType(models.Model):
    name = models.CharField(max_length=100) 

