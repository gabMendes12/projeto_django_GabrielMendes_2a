from django.db import models

# Os modelos das funcionalidades ESG serão adicionados nas próximas entregas.
from django.db import models


class MembroEquipe(models.Model):
    nome = models.CharField(max_length=120)
    papel = models.CharField(max_length=160)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'membro da equipe'
        verbose_name_plural = 'membros da equipe'

    def __str__(self):
        return self.nome


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
