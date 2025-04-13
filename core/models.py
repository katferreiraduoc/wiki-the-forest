from django.db import models

class Usuario(models.Model):
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.correo