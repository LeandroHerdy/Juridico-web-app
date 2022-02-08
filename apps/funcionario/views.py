from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Funcionario, Empresa
from .. import empresa


class FuncionarioList(ListView):
    model = Funcionario
    fields = ['nome', 'cpf', 'empresa', 'departamento']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'cpf', 'empresa', 'departamento']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'cpf', 'empresa', 'departamento']

    def get_queryset(self):
        if not Empresa:
            empresa_logada = self.request.user.funcionario.empresa
            queryset = Empresa.objects.filter(empresa=empresa_logada)
            empresa = queryset
            return ('ok')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=funcionario.nome)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
