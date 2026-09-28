from django.db import models

# Os modelos das funcionalidades ESG serão adicionados nas próximas entregas.
from django.db import models


class MensagemContato(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    assunto = models.CharField(max_length=160)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_envio']
        verbose_name = 'mensagem de contato'
        verbose_name_plural = 'mensagens de contato'

    def __str__(self):
        return f'{self.assunto} — {self.nome}'
