from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)


