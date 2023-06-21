from django import forms
from utilisateur.models import Utilisateur
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import password_validation

class InscriptionForm(UserCreationForm):
    username = forms.CharField(label='Utilisateur :',widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Mot de passe :',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmer le mot de passe :',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='E-mail :',widget=forms.EmailInput(attrs={'class':'form-control'}))
    telephone = forms.CharField(label='Telephone :',widget = forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
         model = Utilisateur
         fields = ['username','last_name','first_name','email','telephone','profile','password1','password2','is_staff']
         
         widgets = {
            'profile': forms.FileInput(attrs={'class':'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={}),
        }
         
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Ancien mot de passe"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'auto-focus':True, 'class':'form-control', 'placeholder':'Current Password'}))
    new_password1 = forms.CharField(label=("Nouveau mot de passe"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'New Password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirmer le mot de passe"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'Confirm Password'}))