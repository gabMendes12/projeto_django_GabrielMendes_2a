from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import View

from .models import Pergunta, Resposta


class MainView(View):
    def get(self, request):
        perguntas = Pergunta.objects.order_by('-data_criacao')
        return render(request, 'forum/index.html', {'perguntas': perguntas})


class PerguntaView(View):
    def get(self, request, pergunta_id):
        try:
            pergunta = Pergunta.objects.get(pk=pergunta_id)
        except Pergunta.DoesNotExist as error:
            raise Http404('Pergunta inexistente') from error

        return render(request, 'forum/detalhe.html', {'pergunta': pergunta})


class VotoView(View):
    def get(self, request, resposta_id):
        try:
            resposta = Resposta.objects.get(pk=resposta_id)
        except Resposta.DoesNotExist as error:
            raise Http404('Resposta inexistente') from error

        return HttpResponse(f'{resposta}; votos: {resposta.votos}')

    def post(self, request, resposta_id):
        try:
            resposta = Resposta.objects.get(pk=resposta_id)
        except Resposta.DoesNotExist as error:
            raise Http404('Resposta inexistente') from error

        resposta.votos += 1
        resposta.save(update_fields=['votos'])
        return redirect(reverse('forum:detalhe', args=[resposta.pergunta.id]))


class InserirPerguntaView(View):
    def get(self, request):
        return render(request, 'forum/inserir_pergunta.html')

    def post(self, request):
        titulo = request.POST.get('titulo', '').strip()
        detalhe = request.POST.get('detalhe', '').strip()
        tentativa = request.POST.get('tentativa', '').strip()

        if not titulo or not detalhe:
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
            detalhe=detalhe,
            tentativa=tentativa,
            data_criacao=timezone.now(),
            usuario=usuario,
        )
        return redirect(reverse('forum:detalhe', args=[pergunta.id]))


class InserirRespostaView(View):
    def get(self, request, pergunta_id):
        try:
            pergunta = Pergunta.objects.get(pk=pergunta_id)
        except Pergunta.DoesNotExist as error:
            raise Http404('Pergunta inexistente') from error

        return render(request, 'forum/inserir_resposta.html', {'pergunta': pergunta})

    def post(self, request, pergunta_id):
        try:
            pergunta = Pergunta.objects.get(pk=pergunta_id)
        except Pergunta.DoesNotExist as error:
            raise Http404('Pergunta inexistente') from error

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
