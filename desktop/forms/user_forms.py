from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from desktop.models.user_models import UserProfile

class UserForm(forms.ModelForm):
    """Formulário para criação de novos usuários."""
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'As senhas não conferem')
        
        return cleaned_data

class UserEditForm(forms.ModelForm):
    """Formulário para edição de usuários existentes."""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff']

class UserProfileForm(forms.ModelForm):
    """Formulário para o perfil de usuário."""
    data_nascimento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    data_contratacao = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = UserProfile
        fields = ['foto', 'telefone', 'cargo', 'departamento', 'data_nascimento', 'data_contratacao', 'cpf', 'observacoes']

class PasswordResetForm(forms.Form):
    """Formulário para redefinição de senha."""
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'As senhas não conferem')
        
        return cleaned_data