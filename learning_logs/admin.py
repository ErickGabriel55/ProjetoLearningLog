from django.contrib import admin
from learning_logs.models import Topic, Entry


# Register your models here.
admin.site.register(Topic) # Registra a tabela no painel do admin.
admin.site.register(Entry)