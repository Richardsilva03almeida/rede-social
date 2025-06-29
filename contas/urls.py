from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair'),
    path('deletar/', views.deletar_conta, name='deletar_conta'),

    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/<str:username>/', views.ver_perfil, name='ver_perfil'),



]
