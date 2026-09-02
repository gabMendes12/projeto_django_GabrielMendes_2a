from django.urls import path

from . import views


app_name = 'esg'

urlpatterns = [
    path('', views.home, name='home'),
]
