from django.db import models

class Menu(models.Model):
    fecha = models.DateField(unique=True)

    def __str__(self):
        return f"Menú para el día {self.fecha}"

class Plato(models.Model):
    plato_entrada = 'entrada'
    plato_principal = 'principal'
    plato_postre = 'postre'

    tipo_platillo = [
        (plato_entrada, 'Entrada'),
        (plato_principal, 'Plato Principal'),
        (plato_postre, 'Postre'),
    ]

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='platos')
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=30, choices=tipo_platillo, default=plato_entrada)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
