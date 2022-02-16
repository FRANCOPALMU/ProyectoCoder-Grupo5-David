from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CargaInstrumento(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    tipoinstrumento = forms.CharField()
    color = forms.CharField()

class CargaDisco(forms.Form):
    artista = forms.CharField (max_length = 35)
    album = forms.CharField (max_length = 35)
    fechaLanzamiento = forms.DateField()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label ='Repertir Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['email','password1','password2','first_name','last_name']
class AvatarFormulario(forms.Form):


    
    imagen = forms.ImageField(required=True)