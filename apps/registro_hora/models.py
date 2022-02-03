from django.db import models


class RegistroHora(models.Model):
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    