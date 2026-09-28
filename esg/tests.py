from django.test import TestCase

from .models import MensagemContato, MembroEquipe


class HomePageTests(TestCase):
    def test_impacta_page_is_available(self):
        response = self.client.get('/impacta/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Impacta ESG')

    def test_root_redirects_to_forum(self):
        response = self.client.get('/')

        self.assertRedirects(response, '/forum/')

    def test_equipe_exibe_membro(self):
        MembroEquipe.objects.get_or_create(
            email='gmc3@cesar.school',
            defaults={
                'nome': 'Gabriel Mendes Cavalcanti',
                'papel': 'Desenvolvimento e documentação',
            },
        )

        response = self.client.get('/impacta/equipe/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Gabriel Mendes Cavalcanti')

    def test_envia_mensagem_de_contato(self):
        response = self.client.post(
            '/impacta/fale-conosco/',
            {
                'nome': 'Ana Silva',
                'email': 'ana@example.com',
                'assunto': 'Dúvida sobre ESG',
                'mensagem': 'Como posso começar?',
            },
        )

        self.assertRedirects(response, '/impacta/fale-conosco/?enviado=1')
        self.assertEqual(MensagemContato.objects.count(), 1)

    def test_rejeita_contato_com_email_invalido(self):
        response = self.client.post(
            '/impacta/fale-conosco/',
            {
                'nome': 'Ana Silva',
                'email': 'email-invalido',
                'assunto': 'Dúvida',
                'mensagem': 'Preciso de ajuda.',
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(MensagemContato.objects.count(), 0)
        self.assertContains(response, 'Informe um e-mail válido.', status_code=400)
