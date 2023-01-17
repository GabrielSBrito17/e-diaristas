from django.urls import path
from .views import *

urlpatterns = [
    path('servico/cadastrar', cadastrar_servico, name='cadastrar_servico'),
    path('servico/listar', listar_servicos, name='listar_servicos'),
    path('servico/editar/<int:id>', editar_servico, name='editar_servico'),
]