from django.shortcuts import render

def index(requisicao):
    contexto = {
        "cursos":[
            {"nome":"Desenvolvimento de Sistemas", "tipo":"Graduação"},
            {"nome":"Banco de Dados", "tipo":"Graduação"},
            {"nome":"Internet Das Coisas", "tipo":"Graduação"},
            {"nome":"TecWeb", "tipo":"Graduação"}
        ],
        "faculdade": "Faculdade Impacta",
        "Pagina":"Homepage",
        "usuario": "Felipe",
        "logado": False,
        "idade": 17
    }
    return render(requisicao, "index.html",contexto)

def cursos(request):
    context = {
        "cursos": [
            {
                "nome": "Graduação em Sistemas de Informação",
                 "alt": "Imagem do Curso de SI",
                 "path": "detalheCurso.html",
                 "img":"img/box_curso_si.jpg"},

            {
                "nome": "Graduação em Administração",
                "alt": "Imagem do Curso de ADM",
                "path": "detalheCurso.html",
                "img":"img/box_curso_adm.jpeg"
            },
            {
                "nome": "Graduação em Banco de Dados",
                "alt": "Imagem do Curso de BD",
                "path": "detalheCurso.html",
                "img":"img/box_curso_bd.jpeg"
            },
            {
                "nome": "Graduação em Análise e Desenvolvimento de Sistemas",
                "alt": "Imagem do Curso de ADS",
                "path": "detalheCurso.html",
                "img":"img/box_curso_ads.jpg"
            },
            {
                "nome": "Graduação em Jogos Digitais",
                "alt": "Imagem do Curso de Jogos",
                "path": "detalheCurso.html",
                "img":"img/box_curso_jogos.jpeg"
            },
            {
                "nome": "Graduação em Gestão da Tecnologia da Informação",
                "alt": "Imagem do Curso de GTI",
                "path": "detalheCurso.html",
                "img":"img/box_curso_gti.jpeg"
            }
        ]
    }
    return render(request, 'cursos.html', context)