from django.db import models

# Create your models here.
# Clase Usuario
class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=150, blank=True, null=True, help_text="Nombre completo o apodo del usuario")
    edad = models.IntegerField(blank=True, null=True, help_text="Edad del usuario")
    email_contacto = models.EmailField(max_length=254, blank=True, null=True, help_text="Dirección de correo electrónico de contacto")

def __str__(self):
        return f'Perfil de {self.usuario.username}'