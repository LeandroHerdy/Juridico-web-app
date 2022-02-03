import uuid

from django.db import models

from apps.empresa.models import Empresa


class Departamento(models.Model):
    id_departamento = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

