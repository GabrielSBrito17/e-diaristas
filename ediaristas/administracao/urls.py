from django.urls import path
from .views import servico_views, usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('servico/cadastrar', servico_views.cadastrar_servico, name='cadastrar_servico'),
    path('servico/listar', servico_views.listar_servicos, name='listar_servicos'),
    path('servico/editar/<int:id>', servico_views.editar_servico, name='editar_servico'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuarios, name='cadastrar_usuarios'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuarios, name='editar_usuario'),
    path('autenticacao/login', auth_views.LoginView.as_view(), name='logar_usuario')
]