from django.urls import path

from . import views


app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pergunta_id>/', views.detalhe, name='detalhe'),
    path('<int:resposta_id>/voto/', views.voto, name='voto'),
    path('inserir/', views.inserir_pergunta, name='inserir_pergunta'),
    path(
        '<int:pergunta_id>/resposta/',
        views.inserir_resposta,
        name='inserir_resposta',
    ),
]
