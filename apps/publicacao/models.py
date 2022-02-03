from django.db import models


class Publicacao(models.Model):
    numero = models.IntegerField(max_length=50)
