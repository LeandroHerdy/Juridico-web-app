import uuid

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.departamento.models import Departamento
from apps.empresa.models import Empresa


class Funcionario(models.Model):
    id_funcionario = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)

    def get_absolute_url(self):
        return reverse('list_funcionario')

    def __str__(self):
        return self.nome


