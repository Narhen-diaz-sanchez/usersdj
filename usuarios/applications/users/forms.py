from django import forms
#
from .models import User
from django.contrib.auth import authenticate


class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña'
            }
        )
    )
    

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')
            
            
class LoginForm(forms.Form):
    Username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'ingrese el usuario'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese la contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['Username']
        password = self.cleaned_data['password']
        
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data
    
    
class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese la contraseña actual'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese la contraseña nueva  '
            }
        )
    )
    
    
class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)
    
    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)
    
    
    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']
        
        if len(codigo) == 6:
            #verificamos si el codigo y el id de usuario son validos
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('El código es incorrecto')
        else:
            raise forms.ValidationError('El código es incorrecto')