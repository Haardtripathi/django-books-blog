from django.db import models
from django.db import connections

# Create your models here.
class book_details(models.Model):
    title=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    rating=models.CharField(max_length=10)
    author=models.CharField(max_length=50)
    yop=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    url=models.CharField(max_length=100) 
    genre=models.CharField(max_length=100)

    class Meta:
        db_table="book_details"

class blogs(models.Model):
    name=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    content=models.TextField(max_length=1000)

    class Meta:
        db_table="blog"

class Insert(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    subject=models.CharField(max_length=50)
    notes=models.CharField(max_length=100)
    class Meta:
        db_table="contacttable"