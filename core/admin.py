from django.contrib import admin
from .models import *

class MatriculaAdmin(admin.ModelAdmin):
    list_filter = ['disciplinaofertada__ano', 'disciplinaofertada__semestre']

# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Periodo)
admin.site.register(GradeCurricular)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(PeriodoDisciplina)
admin.site.register(DisciplinaOfertada)
admin.site.register(Turma)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Questao)
admin.site.register(Resposta)
admin.site.register(ArquivoResposta)
admin.site.register(ArquivoQuestao)

