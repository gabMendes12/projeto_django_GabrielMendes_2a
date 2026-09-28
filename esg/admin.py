from django.contrib import admin

from .models import MensagemContato, MembroEquipe


@admin.register(MembroEquipe)
class MembroEquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'papel', 'email')
    search_fields = ('nome', 'papel', 'email')


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')
    readonly_fields = ('data_envio',)
