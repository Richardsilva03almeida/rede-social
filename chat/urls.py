from django.urls import path
from . import views

urlpatterns = [
    # Página principal do chat (com lista de usuários)
    path('chat_home/', views.chat_view, name='chat_home'),
    
    # Chat com usuário específico
    path('<str:username>/', views.chat_view, name='chat'),
    
    # Edição e exclusão de mensagens
    path('mensagem/<int:pk>/editar/', views.editar_mensagem, name='editar_mensagem'),
    path('mensagem/<int:pk>/apagar/', views.apagar_mensagem, name='apagar_mensagem'),
]