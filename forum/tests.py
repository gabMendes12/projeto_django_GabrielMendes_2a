from django.test import TestCase
from django.utils import timezone

from .models import Pergunta, Resposta


class ForumTests(TestCase):
    def test_lista_sem_perguntas(self):
        response = self.client.get('/forum/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nenhuma pergunta disponível.')

    def test_cria_pergunta(self):
        response = self.client.post(
            '/forum/inserir/',
            {
                'titulo': 'Como começar uma ação ESG?',
                'detalhe': 'Quero organizar as primeiras ações da empresa.',
                'tentativa': 'Ainda estou pesquisando.',
            },
        )

        pergunta = Pergunta.objects.get()
        self.assertRedirects(response, f'/forum/{pergunta.id}/')
        self.assertEqual(pergunta.titulo, 'Como começar uma ação ESG?')

    def test_exibe_detalhe_e_resposta(self):
        pergunta = Pergunta.objects.create(
            titulo='Como medir o consumo de energia?',
            detalhe='Precisamos acompanhar esse indicador.',
            tentativa='Ainda não usamos uma planilha.',
            data_criacao=timezone.now(),
        )

        response = self.client.post(
            f'/forum/{pergunta.id}/resposta/',
            {'texto_resposta': 'Comece registrando o consumo mensal.'},
        )

        self.assertRedirects(response, f'/forum/{pergunta.id}/')
        self.assertEqual(pergunta.resposta_set.count(), 1)
        self.assertContains(
            self.client.get(f'/forum/{pergunta.id}/'),
            'Comece registrando o consumo mensal.',
        )

    def test_vota_em_uma_resposta(self):
        pergunta = Pergunta.objects.create(
            titulo='Como envolver a equipe?',
            detalhe='Quero começar a parte social do projeto.',
            data_criacao=timezone.now(),
        )
        resposta = Resposta.objects.create(
            pergunta=pergunta,
            texto='Faça uma conversa curta com a equipe.',
            data_criacao=timezone.now(),
        )

        response = self.client.post(f'/forum/{resposta.id}/voto/')

        self.assertRedirects(response, f'/forum/{pergunta.id}/')
        resposta.refresh_from_db()
        self.assertEqual(resposta.votos, 1)
