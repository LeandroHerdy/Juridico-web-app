import uuid

from django.db import models
from django.urls import reverse

from apps.empresa.models import Empresa


class Processo(models.Model):
    id_processo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    numero = models.IntegerField(max_length=100)

    def get_absolute_url(self):
        return reverse('list_processo')

    def __int__(self):
        return self.numero
