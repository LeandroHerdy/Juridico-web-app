from django.urls import path
from .views import PublicacaoCreateView, PublicacaoListView,\
    PublicacaoUpdateView, PublicacaoDeleteView

urlpatterns = [
    path('novo/', PublicacaoCreateView.as_view(), name='create_publicacao'),
    path('listar/', PublicacaoListView.as_view(), name='list_publicacao'),
    path('update/<int:pk>/', PublicacaoUpdateView.as_view(), name='update_publicacao'),
    path('delete/<int:pk>/', PublicacaoDeleteView.as_view(), name='delete_publicacao'),
]