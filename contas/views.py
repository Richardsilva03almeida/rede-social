from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EmailLoginForm
from django.contrib.auth.models import User

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha']
            )
            login(request, user)
            return redirect('sobre')
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def entrar(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('chat_home')
    else:
        form = EmailLoginForm()
    return render(request, 'entrar.html', {'form': form})

@login_required
def sair(request):
    logout(request)
    return redirect('entrar')

@login_required
def deletar_conta(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('entrar')
    return render(request, 'deletar.html')



#-----------------------------------------------------------------#

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EmailLoginForm, PerfilForm
from django.contrib.auth.models import User

# Suas views já existentes...


def ver_perfil(request, username):
    user = get_object_or_404(User, username=username)
    perfil = user.perfil
    return render(request, 'ver_perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil', username=request.user.username)
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'editar_perfil.html', {'form': form})
