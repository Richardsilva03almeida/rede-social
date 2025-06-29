from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Mensagem
from django.db.models import Q

User = get_user_model()

@login_required
def chat_view(request, username=None):
    # Lista de usuários (excluindo o usuário atual)
    users = User.objects.exclude(id=request.user.id)
    
    # Variáveis para o chat ativo
    active_user = None
    mensagens = []
    
    # Se um username foi especificado na URL
    if username:
        active_user = get_object_or_404(User, username=username)
        
        # Obter mensagens entre os usuários
        mensagens = Mensagem.objects.filter(
            (Q(sender=request.user) & Q(receiver=active_user)) |
            (Q(sender=active_user) & Q(receiver=request.user))
        ).order_by('timestamp')
        
        # Processar envio de nova mensagem
        if request.method == 'POST':
            texto = request.POST.get('texto')
            if texto:
                Mensagem.objects.create(
                    sender=request.user,
                    receiver=active_user,
                    texto=texto
                )
                return redirect('chat', username=username)
    
    return render(request, 'chat_unificado.html', {
        'users': users,
        'mensagens': mensagens,
        'outro_usuario': active_user,  # Mantive o nome original para compatibilidade
        'active_user': active_user.username if active_user else None
    })

@login_required
def editar_mensagem(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)
    if mensagem.sender != request.user:
        return redirect('chat', username=mensagem.receiver.username)

    if request.method == 'POST':
        novo_texto = request.POST.get('texto')
        if novo_texto:
            mensagem.texto = novo_texto
            mensagem.save()
        return redirect('chat', username=mensagem.receiver.username)

@login_required
def apagar_mensagem(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)
    if mensagem.sender == request.user:
        mensagem.delete()
    return redirect('chat', username=mensagem.receiver.username)

#-----------------------------------------------------------------#