from django.db import models

# Create your models here.

# Usuário cria os tópicos
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text

"""Anotações do usuário sobre os tópicos. Possui uma relação de um para muitos, já que um tópico pode ter várias anotações"""
class Entry(models.Model):
    """Algo específiico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text[:50] + '...'