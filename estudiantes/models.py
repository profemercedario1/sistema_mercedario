from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("puede_editar", "Puede editar estudiantes"),
            ("puede_eliminar", "Puede eliminar estudiantes"),
        ]
