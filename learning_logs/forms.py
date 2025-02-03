from django import forms # uma variedade de classes e funções que facilitam a definição, renderização e validação de formulários em suas aplicações web.
from .models import Topic# Topic é um dos bancos de dados que está em models

class TopicForm(forms.ModelForm):
    class Meta(): # classe que especifica o banco de dados
        model = Topic # banco de dados associado ao formulário
        fields = ['text'] # Campos do modelo que serão incluídos no formulário
        labels = {'text': ''} # especifica para o django que não é para ter rótulos