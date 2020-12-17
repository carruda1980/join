import datetime

from django.db import models


class UserLocation(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)

    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    data_expiracao = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.nome