"""Define padrões de URL para learning_logs."""

from django.urls import path, include

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    # Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),

    # Pagina de detalhes para um unico assunto
    path('topics/<int:topic_id>', views.topic, name='topic'),

    # Pagina para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),
]