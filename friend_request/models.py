from django.db import models

# Create your models here.


class FriendRequestModel(models.Model):
    id = models.AutoField(primary_key=True)
    request_from = models.CharField(max_length=16)
    request_to = models.CharField(max_length=16)
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'friend_request'
