from django.shortcuts import render

# Create your views here.
def index(request):
    """Página principal do learning_log"""
    return render(request, 'learning_logs/index.html')