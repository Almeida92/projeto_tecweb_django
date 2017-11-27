from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField("Nome", max_length=50)
    carga_horaria = models.IntegerField("Carga Horária")
    professor = models.CharField("Coordenador", max_length=50)
    tipo = models.CharField(max_length=50)
    img = models.CharField(max_length=255, blank=True)
    descricao = models.TextField("Descrição", blank=True)
    ativo = models.BooleanField("Ativo?", default=True)

class Aluno(models.Model):
    ra = models.IntegerField("RA Aluno")
    nome = models.CharField("Nome", max_length=120)
    email = models.CharField("E-Mail",max_length=80)
    celular = models.CharField("Celular",max_length=11)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome