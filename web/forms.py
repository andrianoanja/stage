from django import forms
from web.models import *

class SecteurForm(forms.ModelForm):
    codeSect = forms.CharField(label='Code Secteur :',widget = forms.TextInput(attrs={'class':'form-control'}))
    secteur = forms.CharField(label='Secteur :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Secteur 
        fields = ['codeSect','secteur']
        
class FiliereForm(forms.ModelForm):
    codeF = forms.CharField(label='Code Filière :',widget = forms.TextInput(attrs={'class':'form-control'}))
    filiere = forms.CharField(label='Filière :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # secteur = forms.CharField(label='Secteur :',widget = forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Filiere
        fields = ['codeF','filiere','secteur']
        widgets = {
            'secteur': forms.Select(attrs={'class':'form-control'}),
        }
        labels={'secteur':'Secteur'}


        
class ClasseForm(forms.ModelForm):
    codeC = forms.CharField(label='Code Classe :',widget = forms.TextInput(attrs={'class':'form-control'}))
    classe = forms.CharField(label='Classe :',widget = forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta:
        model= Classe
        fields=['codeC','filiere','niveau','type_formation','classe']
        widgets = {
            'filiere'  :   forms.Select(attrs={'class':'form-control'}),
            'niveau'  :   forms.Select(attrs={'class':'form-control'}),
            'type_formation'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={
            'niveau' :'Niveau',
            'filiere':'Filière',
            'type_formation' :'Type formation',
            }
        
class EtudiantForm(forms.ModelForm):
    # sport_pratique = forms.CharField(label='Sport Pratiqué :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # sport_preferer = forms.CharField(label='Sport Preferer :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # nombre_de_frere = forms.CharField(label='Nombre Frère :',widget = forms.NumberInput(attrs={'class':'form-control'}))
    # nombre_de_soeur = forms.CharField(label='Nombre Soeur :',widget = forms.NumberInput(attrs={'class':'form-control'}))
    # rang_dans_la_famille = forms.CharField(label='Rang dans la famille :',widget = forms.NumberInput(attrs={'class':'form-control'}))
    # adresse_des_correspondant = forms.CharField(label='Adresse :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # profession_correspondant = forms.CharField(label='Profession :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # nom_du_correspondant = forms.CharField(label='Correspondant :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # adresse_des_parents = forms.CharField(label='Adresse des Parents :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # ecole_origine = forms.CharField(label='Ecole d origine :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # numero = forms.CharField(label='Numero :',widget = forms.TextInput(attrs={'class':'form-control'}))
    date_de_naissance = forms.DateField(label='Date de naissance :',widget = forms.TextInput(attrs={'class':'form-control','type':'date'}))
    nom = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # telephone = forms.CharField(label='Telephone :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.CharField(label='E-mail :',widget = forms.EmailInput(attrs={'class':'form-control'}))
    # adresse = forms.CharField(label='Adresse :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # image = forms.ImageField(label='Photo :',widget = forms.FileInput(attrs={'class':'form-control'}))
    # nom_du_pere = forms.CharField(label='Père :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # profession_pere = forms.CharField(label='Profession :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # nom_de_la_mere = forms.CharField(label='Mère :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # profession_mere = forms.CharField(label='Profession :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Etudiant 
        fields =  ['nom','prenom','date_de_naissance', 'sexe']
        widgets = {
            'sexe'  :   forms.Select(attrs={'class':'form-control'}),
            # 'promotion'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={
            'sexe' :'Sexe',
            # 'promotion':'Promotion',
            
            }
        
class PeriodeForm(forms.ModelForm):
    codeP = forms.CharField(label='Code Période :',widget = forms.TextInput(attrs={'class':'form-control'}))
    periode = forms.CharField(label='Période :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Periode
        fields = ['codeP','periode']
        
class AnneeScoForm(forms.ModelForm):
    codeAS = forms.CharField(label='Code Année Scolaire :',widget = forms.TextInput(attrs={'class':'form-control'}))
    annee_scolaire = forms.CharField(label='Année Scolaire :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = AnneeScolaire
        fields = ['codeAS','annee_scolaire']
        
class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['niveau','filiere','matiere','coeff']
        widgets = {
            'coeff'  :   forms.NumberInput(attrs={'class':'form-control'}),
            'niveau'  :   forms.Select(attrs={'class':'form-control'}),
            'filiere'  :   forms.Select(attrs={'class':'form-control'}),
            'matiere'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={'coeff'  :'Coeffiant',
                'niveau':'Niveau',
                'filiere':'Filière',
                'matiere':'Matiere',
                }

class TypeMatiereForm(forms.ModelForm):
    type_matiere = forms.CharField(label='Type Matière :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = TypeMatiere
        fields = ['type_matiere']
        
class TypeFormationForm(forms.ModelForm):
    codeTF = forms.CharField(label='Code Type Formation :',widget = forms.TextInput(attrs={'class':'form-control'}))
    type_formation = forms.CharField(label='Type Formation :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = TypeFormation
        fields= ['codeTF','type_formation']
        
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['periode','matiere']
        widgets = {
            'periode'  :   forms.Select(attrs={'class':'form-control'}),
            'matiere'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={'periode'  :'Periode',
                'matiere':'Matière'
                }

class Contenirform(forms.ModelForm):
    # etudiant = forms.CharField(label='Etudiant :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Contenir
        fields=['DS1','DS2','exam']
        widgets = {
            'DS1'  :   forms.NumberInput(attrs={'class':'form-control','min':'0' ,'max':'20'}),
            'DS2'  :   forms.NumberInput(attrs={'class':'form-control','min':'0' ,'max':'20'}),
            'exam'  :   forms.NumberInput(attrs={'class':'form-control','min':'0' ,'max':'20'}),
        }
        labels={'DS1'  :'DS1',
                'DS2':'DS2',
                'exam':'Exam'
                }

class MatForm(forms.ModelForm):
    matier = forms.CharField(label='Matière :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Matier
        fields=['matier','type_matiere']  
        widgets = {
            'type_matiere'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={'type_matiere'  :'Type Matiere',
                }