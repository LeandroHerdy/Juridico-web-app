from django.db import models


class Processo(models.Model):
    numero = models.IntegerField(max_length=100)
