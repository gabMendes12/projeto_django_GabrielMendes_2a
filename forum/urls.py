from django.urls import path

from . import views


app_name = 'forum'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('<int:pergunta_id>/', views.PerguntaView.as_view(), name='detalhe'),
    path('<int:resposta_id>/voto/', views.VotoView.as_view(), name='voto'),
    path('inserir/', views.InserirPerguntaView.as_view(), name='inserir_pergunta'),
    path(
        '<int:pergunta_id>/resposta/',
        views.InserirRespostaView.as_view(),
        name='inserir_resposta',
    ),
]
