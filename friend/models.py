from django.db import models

# Create your models here.

class FriendModel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=16)
    friend_id = models.CharField(max_length=16)
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'friend'