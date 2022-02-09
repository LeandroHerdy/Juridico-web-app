import uuid

from django.db import models
from django.urls import reverse

from apps.empresa.models import Empresa


class Departamento(models.Model):
    id_departamento = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('list_departamento')

    def __str__(self):
        return self.nome
