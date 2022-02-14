from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Publicacao
from django.urls import reverse_lazy

from .. import publicacao
from ..empresa.models import Empresa
from ..processo.models import Processo


class PublicacaoListView(ListView):
    queryset = Publicacao.objects.all()
    context_object_name = 'Processo'
    template_name = 'processo_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        processos = Processo.objects.filter(empresa=empresa_logada)
        for processo in processos:
            queryset = Publicacao.objects.filter(processo=processo)
            return queryset


class PublicacaoUpdateView(UpdateView):
    models = Publicacao
    fields = ['numero']


class PublicacaoDeleteView(DeleteView):
    models = Publicacao
    success_url = reverse_lazy('list_publicacao')
