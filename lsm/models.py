from django.db import models

# Create your models here.
class Book(models.Model):
    B_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    author=models.CharField()
    pages=models.IntegerField()
    status=models.BooleanField(default=True)