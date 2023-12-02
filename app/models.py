from django.db import models

# Create your models here.

class Product_Categories(models.Model):
    CategorieName=models.CharField(max_length=100)
    Categorieid=models.PositiveIntegerField()

    def __str__(self):
        return self.CategorieName

class Product(models.Model):
    CategorieName=models.ForeignKey(Product_Categories,on_delete=models.CASCADE)
    PName=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=8,decimal_places=2)
    Pid=models.PositiveIntegerField(primary_key=True)
    Date=models.DateField()

    def __str__(self):
        return self.PName