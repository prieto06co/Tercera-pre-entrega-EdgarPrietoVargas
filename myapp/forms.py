from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()

class ComponenteFormulario(forms.Form):
    nombre = forms.CharField()
    cantidad = forms.IntegerField()

class SedeFormulario(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    nro_tel = forms.CharField()

class ColaboradorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()