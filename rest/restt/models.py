from django.db import models

# Create your models here.
class Store(models.Model):
    Firstname=models.CharField("enter your first name",max_length=100)
    Lastname=models.CharField("enter you last name",max_length=100)
    contact=models.IntegerField(("enter your number"))
    Email=models.EmailField(("enter your email"), max_length=254)
    
    def __str__(self) -> str:
        return self.Firstname+" "+self.Lastname