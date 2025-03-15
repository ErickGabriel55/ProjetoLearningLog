from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # direciona para a função index. o name foi definido no base.html.
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
