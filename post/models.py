from django.db import models

# Create your models here.

class PostModel(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    content = models.TextField()
    user_id = models.CharField(max_length=16)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    class Meta:
        db_table = 'post'
