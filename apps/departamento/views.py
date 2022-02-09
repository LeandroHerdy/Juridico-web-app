from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from apps.departamento.models import Departamento


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)


class DepartamentoList(ListView):
    models = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_logada)
        return queryset


class DepartamentoEdit(UpdateView):
    model = ['nome']


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamento')



