from django.urls import path

from apps.departamento.views import DepartamentoList, DepartamentoCreate, DepartamentoDelete, DepartamentoEdit

urlpatterns = [
    path('listar/', DepartamentoList.as_view(), name='list_departamento'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),
    path('update/<int:pk>', DepartamentoEdit.as_view(), name='update_departamento'),
]
