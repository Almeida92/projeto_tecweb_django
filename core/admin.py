from django.contrib import admin
from .models import Curso,Aluno,Periodo,GradeCurricular,Professor,Disciplina,PeriodoDisciplina,DisciplinaOfertada,Turma

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