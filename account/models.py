from django.db import models

# Create your models here.

class AccountModel(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    user_id = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    class Meta:
        db_table = 'account'
