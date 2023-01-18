from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def cadastrar_usuarios(request):
    form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})