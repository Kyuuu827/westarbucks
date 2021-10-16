from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    K_name = models.CharField(max_length=45)
    E_name = models.CharField(max_length=45)
    description = models.TextField()
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'images'

class Allegy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allegy'

class Allegy_product(models.Model):
    allegy = models.ForeignKey('Allegy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allegy_products'