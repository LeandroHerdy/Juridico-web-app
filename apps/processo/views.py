from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Processo
from ..empresa.models import Empresa


class ProcessoCreateView(CreateView):
    model = Processo
    fields = ['numero']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Empresa.objects.filter(empresa=empresa_logada)
        empresa = queryset
        return 'ok'


class ProcessoListView(ListView):
    queryset = Processo.objects.all()
    context_object_name = 'processo'
    template_name = 'processo/processo_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Processo.objects.filter(empresa=empresa_logada)
        return queryset


class ProcessoUpdateView(UpdateView):
    model = Processo
    fields = ['numero']


class ProcessoDeleteView(DeleteView):
    models = Processo
    success_url = reverse_lazy('list_processo')