from django.db import models


class Transactions (models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.CharField(max_length=70, null=True, blank=True)
    to_user = models.CharField(max_length=70, null=True, blank=True)
    block_number = models.IntegerField()
    hash = models.CharField(max_length=100, null=True, blank=True)
