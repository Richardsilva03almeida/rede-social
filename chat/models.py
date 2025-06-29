from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensagem(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    texto = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"De {self.sender.username} para {self.receiver.username} - {self.texto[:20]}"