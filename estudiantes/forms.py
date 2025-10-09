# 📄 estudiantes/forms.py
from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    """
    Formulario para registrar estudiantes con nombre y tres notas.
    Calcula el promedio automáticamente al guardar.
    """
    class Meta:
        model = Estudiante
        fields = ['nombre', 'nota1', 'nota2', 'nota3']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del estudiante'
            }),
            'nota1': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ej: 8.50'
            }),
            'nota2': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ej: 7.00'
            }),
            'nota3': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ej: 9.00'
            }),
        }

    def clean(self):
        """
        Validación adicional: asegurar que las notas sean entre 0 y 10.
        """
        cleaned_data = super().clean()
        for nota in ['nota1', 'nota2', 'nota3']:
            valor = cleaned_data.get(nota)
            if valor is not None and (valor < 0 or valor > 10):
                raise forms.ValidationError(f"La {nota} debe estar entre 0 y 10.")
        return cleaned_data
