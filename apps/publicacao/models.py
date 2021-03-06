import uuid

from django.db import models
from django.urls import reverse

from apps.processo.models import Processo


class Publicacao(models.Model):
    id_publicacao = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    processo = models.ForeignKey(Processo, on_delete=models.PROTECT)
    numero = models.IntegerField(max_length=50)

    def get_absolute_url(self):
        return reverse('list_publicacao')

    def __int__(self):
        return self.numero
