from django.db import models

# Create your models here.


class Desejos(models.Model):
    nomeUser = models.CharField(max_length=80)
    nomeLista = models.CharField(max_length=80)
    url = models.URLField()
    email = models.EmailField()
    percent = models.IntegerField(default=5)
    
    def __str__(self):
        return self.nomeUser
    
    
class Item(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    lista = models.ForeignKey(Desejos, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    minPrice = models.IntegerField()
    priceDayAdd = models.IntegerField(default=0)
    dateCreated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title