from django.db import models
from django.contrib import admin
import datetime
from decimal import Decimal

# Create your models here.
class Curso(models.Model):
    nome = models.CharField("Nome", max_length=50)
    carga_horaria = models.IntegerField("Carga Horária")
    professor = models.CharField("Coordenador", max_length=50)
    tipo = models.CharField(max_length=50)
    img = models.CharField(max_length=255, blank=True)
    descricao = models.TextField("Descrição", blank=True)
    ativo = models.BooleanField("Ativo?", default=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    ra = models.IntegerField("RA Aluno")
    nome = models.CharField("Nome", max_length=120)
    email = models.CharField("E-Mail",max_length=80)
    celular = models.CharField("Celular",max_length=11)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    ra = models.IntegerField("RA")
    apelido = models.CharField("Apelido",max_length=30,unique=True)
    nome = models.CharField("Nome",max_length=120)
    email = models.CharField("E-Mail",max_length=80)
    celular = models.CharField("Celular",max_length=11)

    def __str__(self):
        return self.apelido


class GradeCurricular(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ano = models.IntegerField("Ano")
    semestre = models.IntegerField("Semestre")

    def __str__(self):  
        return "Ano " + str(self.ano)+ "-" + "Semestre " +str(self.semestre) + "°"
    
class Periodo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero = models.IntegerField("Numero")
    
    def __str__(self):
        return self.curso.nome + " - " +self.numero
    

class Disciplina(models.Model):
    nome = models.CharField("Nome",max_length=240)
    carga_horaria = models.IntegerField("Carga_Horaria")
    teoria = models.DecimalField("Teoria",max_digits=3,decimal_places=2)
    pratica = models.DecimalField("Pratica",max_digits=3,decimal_places=2)
    ementa = models.TextField("Ementa")
    competencias = models.TextField("Competencias")
    habilidades = models.TextField("Habilidades")
    conteudo = models.TextField("Conteudo")
    bibliografia_basica = models.TextField("Bibliografia Basica")
    bibliografia_complementar = models.TextField("Bibliografia Complementar")

    def __str__(self):
        return self.nome

class PeriodoDisciplina(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.periodo.numero + " - "+self.disciplina.nome

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    ano = models.IntegerField("Ano")
    semestre = models.IntegerField("Semestre")

    def __str__(self):
        return self.disciplina.nome
    
class Turma(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    discplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turno = models.CharField("Turno",max_length=15)

    def __str__(self):
        return self.disciplina.nome + " - " +self.professor.nome

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE)
    Turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.nome

class Questao (models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_limite = models.DateField("Data Limite")
    descricao = models.TextField("Descricao")
    data = models.DateField("Data")

    def __str__(self):
        return str(self.descricao)

class Resposta(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, default=1)
    data_avaliacao = models.DateField("Data Avaliação", default=datetime.date.today)
    nota = models.IntegerField("NOTA", default=0)
    data_envio = models.DateField("Data Envio", default=datetime.date.today)

    def __str__(self):
        return str(self.questao.descricao)

class ArquivoQuestao(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.questao.data) + " - " + str(self.questao.descricao)

class ArquivoResposta(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)        
    Aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)  

    def __str__(self):
        return str(self.questao.data_turma) + " - " + str(self.Aluno.nome)      

    





    


    
    
    