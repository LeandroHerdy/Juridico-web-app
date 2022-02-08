from django.urls import path
from .views import FuncionarioEdit, FuncionarioList, FuncionarioDelete, FuncionarioCreate


urlpatterns = [
    path('listar/', FuncionarioList.as_view(), name='list_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('novo', FuncionarioCreate.as_view(), name='create_funcionario'),
]
