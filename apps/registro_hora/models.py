import uuid

from django.db import models

from apps.funcionario.models import Funcionario


class RegistroHora(models.Model):
    id_registro_hora = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __repr__(self):
        return self.id_registro_hora
