from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Perfil

class RegistroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data

class EmailLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha')

        if email and senha:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Email ou senha inválidos.")

            user = authenticate(username=user.username, password=senha)
            if user is None:
                raise forms.ValidationError("Email ou senha inválidos.")

            self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user
    


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['numero', 'foto', 'curso', 'tipo_usuario']
