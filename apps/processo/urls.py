from django.urls import path
from .views import ProcessoListView, ProcessoCreateView,\
    ProcessoUpdateView, ProcessoDeleteView


urlpatterns = [
    path('novo/', ProcessoCreateView.as_view(), name='create_processo'),
    path('listar/', ProcessoListView.as_view(), name='list_processo'),
    path('update/<int:pk>/', ProcessoUpdateView.as_view(), name='update_processo'),
    path('delete/<int:pk>/', ProcessoDeleteView.as_view(), name='delete_processo'),
]

