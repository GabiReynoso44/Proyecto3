from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=25)
    camada = models.IntegerField()

class Estudiantes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()    


class Profesores(models.Model):

    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()
    email = models.EmailField()    