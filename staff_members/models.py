from django.db import models
from django.contrib.auth.models import User


class Staff_member(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.firstname} {self.lastname}"
# Create your models here.
    
