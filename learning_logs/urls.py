from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # direciona para a função index. o name foi definido no base.html.
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic') # Essa é uma url dinamica, pois recebe um parametro (id de Topic, nesse caso) vindo do models para que não precisemos criar uma rota pra cada tópico.
]
