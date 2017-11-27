from django.shortcuts import render
from core.models import Curso

def index(requisicao):
    contexto = {
        "cursos": Curso.objects.all(),
        "faculdade": "Faculdade Impacta",
        "Pagina":"Homepage",
        "usuario": "Felipe",
        "logado": False,
        "idade": 17,
        "home_activate": True
    }
    return render(requisicao, "index.html",contexto)

def cursos(request):
    context = {
        "cursos": Curso.objects.all(),
        "cursos_activate": True
    }
    return render(request, 'cursos.html', context)

def noticias(request):
    context = {
        ##"cursos": Curso.objects.all(),
        "noticias_activate": True
    }
    return render(request, 'noticias.html', context)