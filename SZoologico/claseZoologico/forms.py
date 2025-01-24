from django import forms

class MiFormulario(forms.Form):
    usuario = forms.CharField(max_length=100, label="Usuario")
    contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
