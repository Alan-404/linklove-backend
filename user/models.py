from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=7)
    phone = models.CharField(max_length=12)
    country = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    avatar = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    class Meta:
        db_table = 'user'
