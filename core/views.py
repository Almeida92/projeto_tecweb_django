from django.shortcuts import render
from core.models import Curso

def index(requisicao):
    contexto = {
        "cursos": Curso.objects.all(),
        "faculdade": "Faculdade Impacta",
        "Pagina":"Homepage",
        "usuario": "Felipe",
        "logado": False,
        "idade": 17
    }
    return render(requisicao, "index.html",contexto)

def cursos(request):
    context = {
        "cursos": Curso.objects.all()
    }
    return render(request, 'cursos.html', context)