from django.db import models

# Create your models here.

class HobbyModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    image = models.TextField()
    class Meta:
        db_table = 'hobby'
