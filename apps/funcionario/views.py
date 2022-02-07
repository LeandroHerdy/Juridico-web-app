from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Funcionario


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome']
