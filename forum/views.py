from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

from .models import Pergunta, Resposta


def index(request):
    perguntas = Pergunta.objects.order_by('-data_criacao')
    busca = request.GET.get('busca', '').strip()
    busca_foi_enviada = 'busca' in request.GET

    if busca_foi_enviada and not busca:
        return render(
            request,
            'forum/index.html',
            {
                'perguntas': perguntas,
                'erro_busca': 'Digite um termo antes de pesquisar.',
            },
            status=400,
        )

    if busca:
        perguntas = perguntas.filter(
            Q(titulo__icontains=busca) | Q(detalhe__icontains=busca)
        )

    return render(
        request,
        'forum/index.html',
        {
            'perguntas': perguntas,
            'busca': busca,
            'busca_foi_enviada': busca_foi_enviada,
        },
    )


def detalhe(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNotExist as error:
        raise Http404('Pergunta inexistente') from error

    return render(request, 'forum/detalhe.html', {'pergunta': pergunta})


def voto(request, resposta_id):
    try:
        resposta = Resposta.objects.get(pk=resposta_id)
    except Resposta.DoesNotExist as error:
        raise Http404('Resposta inexistente') from error

    if request.method == 'GET':
        return HttpResponse(f'{resposta}; votos: {resposta.votos}')

    resposta.votos += 1
    resposta.save(update_fields=['votos'])
    return redirect(reverse('forum:detalhe', args=[resposta.pergunta.id]))


def inserir_pergunta(request):
    if request.method == 'GET':
        return render(request, 'forum/inserir_pergunta.html')

    titulo = request.POST.get('titulo', '').strip()
    detalhe_pergunta = request.POST.get('detalhe', '').strip()
    tentativa = request.POST.get('tentativa', '').strip()

    if not titulo or not detalhe_pergunta:
        return render(
            request,
            'forum/inserir_pergunta.html',
            {
                'erro': 'Preencha o título e o detalhe da pergunta.',
                'dados': request.POST,
            },
            status=400,
        )

    usuario = request.user.username if request.user.is_authenticated else 'anônimo'
    pergunta = Pergunta.objects.create(
        titulo=titulo,
        detalhe=detalhe_pergunta,
        tentativa=tentativa,
        data_criacao=timezone.now(),
        usuario=usuario,
    )
    return redirect(reverse('forum:detalhe', args=[pergunta.id]))


def inserir_resposta(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNotExist as error:
        raise Http404('Pergunta inexistente') from error

    if request.method == 'GET':
        return render(request, 'forum/inserir_resposta.html', {'pergunta': pergunta})

    texto = request.POST.get('texto_resposta', '').strip()
    if not texto:
        return render(
            request,
            'forum/inserir_resposta.html',
            {'pergunta': pergunta, 'erro': 'Escreva uma resposta.'},
            status=400,
        )

    usuario = request.user.username if request.user.is_authenticated else 'anônimo'
    pergunta.resposta_set.create(
        texto=texto,
        data_criacao=timezone.now(),
        usuario=usuario,
    )
    return redirect(reverse('forum:detalhe', args=[pergunta.id]))
