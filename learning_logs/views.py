from django.shortcuts import render 
from .models import Topic

# Create your views here.
def index(request):
    """Página principal do learning_log"""
    return render(request, 'learning_logs/index.html') # O django possui a pasta de caminho templates pré configurada no arquivo settings.py então só precisa passar o resto do caminho

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added') # acessando o banco de dados. Pegando o que ta la em Topic através do object ordenando pela data (Campo da Topic).
    context = {'topics': topics} # Esse dicionário é necessário quando precisamos enviar dados coletados do banco (como o nosso topics acima) para uma página html.
    return render(request, 'learning_logs/topics.html', context) # o context precisa ser retornado junto com request e a página html.

def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)