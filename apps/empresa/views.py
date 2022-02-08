from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from apps.empresa.models import Empresa


class EmpresaCreate(CreateView):
    models = Empresa
    fields = ['nome', 'cnpj']

