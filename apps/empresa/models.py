import uuid

from django.db import models


class Empresa(models.Model):
    id_empresa = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=50, help_text="Nome da Empresa")
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
