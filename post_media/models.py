from django.db import models

# Create your models here.
class PostMediaModel(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.CharField(max_length=60)
    media_link = models.TextField()
    class Meta:
        db_table = 'post_media'