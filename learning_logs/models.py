from django.db import models

# Create your models here.

# Usuário cria os tópicos
class Topic(models.Model): # sempre irá herdar o models.Model. A classe irá ser uma tabela e cada atributo um campo dessa tabela.

    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200) # Campo do tipo texto com número máximo de caracteres
    date_added = models.DateTimeField(auto_now=True) # Campo do tipo data para adicionar e atualiza para sempre para a data atual.
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text

"""Anotações do usuário sobre os tópicos. Possui uma relação de um para muitos, já que um tópico pode ter várias anotações"""
class Entry(models.Model):
    """Algo específiico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Uma chave estrangeira que relaciona cada entrada (anotação) com um tópico e caso o tópico seja deletado as entradas também serão, por conta do on_delete=models.CASCADE.
    text = models.TextField() # Campo de texto maior.
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries' # Para que o django use o plural corretamente.

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text[:50] + '...'