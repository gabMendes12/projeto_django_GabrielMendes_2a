from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import MensagemContato, MembroEquipe


def home(request):
    return render(request, 'esg/home.html')


def redirecionar_para_forum(request):
    return redirect('forum:index')


def equipe(request):
    membros = MembroEquipe.objects.all()
    return render(request, 'esg/equipe.html', {'membros': membros})


def fale_conosco(request):
    if request.method == 'GET':
        return render(request, 'esg/fale_conosco.html', {'enviado': request.GET.get('enviado') == '1'})

    dados = {
        'nome': request.POST.get('nome', '').strip(),
        'email': request.POST.get('email', '').strip(),
        'assunto': request.POST.get('assunto', '').strip(),
        'mensagem': request.POST.get('mensagem', '').strip(),
    }
    erros = {}

    for campo in ('nome', 'email', 'assunto', 'mensagem'):
        if not dados[campo]:
            erros[campo] = 'Este campo é obrigatório.'

    if dados['email']:
        try:
            validate_email(dados['email'])
        except ValidationError:
            erros['email'] = 'Informe um e-mail válido.'

    if erros:
        return render(
            request,
            'esg/fale_conosco.html',
            {'dados': dados, 'erros': erros},
            status=400,
        )

    MensagemContato.objects.create(**dados)
    return redirect(f'{reverse("esg:fale_conosco")}?enviado=1')
