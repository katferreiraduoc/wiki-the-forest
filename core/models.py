from django.contrib.auth.models import User as DjangoUser
from django.db import models

class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username