from django.db import models
from curriculo.models.disciplinas import Disciplina

__alunos__ = ["aluno_1@aluno.faculdadeimpacta.com.br",
              "aluna_2@aluno.faculdadeimpacta.com.br"]


class Curso(models.Model):
    '''
    Classe Curso
    '''
    nome = models.CharField(max_length=255, unique=True)
    sigla = models.CharField(max_length=5, unique=True)
    disciplinas = models.ManyToManyField(Disciplina,
                                         through='MatrizCurricular')
    semestres = models.IntegerField(default=4)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    def monta_matriz(self):
        '''
        Monta um dicionário com as chaves sendo o semestre do curso
        e o valor uma lista de disciplinas que pertencem a aquele
        semestre.
        '''
        matriz = {}
        for i in range(1, self.semestres + 1):
            matriz[i] = []
        for disciplina in self.matrizcurricular_set.all():
            matriz[disciplina.semestre].append(disciplina.disciplina)
        return matriz


class MatrizCurricular(models.Model):
    '''
    Classe Matriz Curricular realizada para o relacionamento
    entre Curso e Disciplina.
    '''
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    disciplina = models.ForeignKey(Disciplina,
                                   on_delete=models.SET_NULL,
                                   null=True)
    semestre = models.IntegerField()
