from django import forms

class Formulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   apellido = forms.CharField(required=True, max_length=64)
   email = forms.CharField(required=True) 
   dni = forms.IntegerField(required=True) 
   telefono = forms.IntegerField(required=True)
   
   





