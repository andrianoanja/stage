from django import forms
from web.models import *

class SecteurForm(forms.ModelForm):
    codeSect = forms.CharField(label='Code Secteur :',widget = forms.TextInput(attrs={'class':'form-control'}))
    secteur = forms.CharField(label='Secteur :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Secteur 
        fields = ['codeSect','secteur']

class SecteurForm1(forms.ModelForm):
    secteur = forms.CharField(label='Secteur :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Secteur 
        fields = ['secteur']

class ProvForm(forms.ModelForm):
    nom = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Proviseur
        fields = ['nom','prenom']

class CenseurForm(forms.ModelForm):
    nom = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Censeur
        fields = ['nom','prenom']
class ChefForm(forms.ModelForm):
    nom = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = ChefDeTravaux
        fields = ['nom','prenom','sexe']
        widgets = {
            'sexe': forms.Select(attrs={'class':'form-control'}),
        }
        labels={'sexe':'Sexe'}
        
class SgForm(forms.ModelForm):
    nom = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = SG
        fields = ['nom','prenom','sexe']
        widgets = {
            'sexe': forms.Select(attrs={'class':'form-control'}),
        }
        labels={'sexe':'Sexe'}
        
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

class FiliereForm1(forms.ModelForm):
    # codeF = forms.CharField(label='Code Filière :',widget = forms.TextInput(attrs={'class':'form-control'}))
    filiere = forms.CharField(label='Filière :',widget = forms.TextInput(attrs={'class':'form-control'}))
    # secteur = forms.CharField(label='Secteur :',widget = forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Filiere
        fields = ['filiere','secteur']
        widgets = {
            'secteur': forms.Select(attrs={'class':'form-control'}),
        }
        labels={'secteur':'Secteur'}

class ResponsableForm(forms.ModelForm):
    nom = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='Prènoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Responsable
        fields=['nom','prenom']
        
class ClasseForm(forms.ModelForm):
    codeC = forms.CharField(label='Code Classe :',widget = forms.TextInput(attrs={'class':'form-control'}))
    classe = forms.CharField(label='Classe :',widget = forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta:
        model= Classe
        fields=['codeC','filiere','niveau','type_formation','responsable','classe']
        widgets = {
            'filiere'  :   forms.Select(attrs={'class':'form-control'}),
            'niveau'  :   forms.Select(attrs={'class':'form-control'}),
            'type_formation'  :   forms.Select(attrs={'class':'form-control'}),
            'responsable'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={
            'niveau' :'Niveau',
            'filiere':'Filière',
            'type_formation' :'Type formation',
            'responsable' :'Responsable',
            }

class ClasseForm1(forms.ModelForm):
    # codeC = forms.CharField(label='Code Classe :',widget = forms.TextInput(attrs={'class':'form-control'}))
    classe = forms.CharField(label='Classe :',widget = forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta:
        model= Classe
        fields=['filiere','niveau','type_formation','responsable','classe']
        widgets = {
            'filiere'  :   forms.Select(attrs={'class':'form-control'}),
            'niveau'  :   forms.Select(attrs={'class':'form-control'}),
            'type_formation'  :   forms.Select(attrs={'class':'form-control'}),
            'responsable'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={
            'niveau' :'Niveau',
            'filiere':'Filière',
            'type_formation' :'Type formation',
            'responsable' :'Responsable',
            }

class EtudiantForm(forms.ModelForm):
   
    ecole_origine = forms.CharField(label='Ecole d origine :',widget = forms.TextInput(attrs={'class':'form-control'}))
    date_de_naissance = forms.DateField(label='Date de naissance :',widget = forms.TextInput(attrs={'class':'form-control','type':'date'}))
    nom = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    adresse = forms.CharField(label='Adresse :',widget = forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(label='Photo :',widget = forms.FileInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Etudiant
        fields =  ['nom','prenom','date_de_naissance', 'sexe','position','telephone','email','adresse','image','ecole_origine','nom_du_pere','profession_pere','nom_de_la_mere','profession_mere','adresse_des_parents','nom_du_correspondant','profession_correspondant','adresse_des_correspondant','nombre_de_frere','nombre_de_soeur','rang_dans_la_famille','sport_preferer','sport_pratique']
        widgets = {
            'sexe'  :   forms.Select(attrs={'class':'form-control'}),
            'position'  :   forms.Select(attrs={'class':'form-control'}),
            'telephone'  :   forms.TextInput(attrs={'class':'form-control','id':'phone'}),
            'email'  :   forms.TextInput(attrs={'class':'form-control','type':'email'}),
            'nom_du_pere'  :   forms.TextInput(attrs={'class':'form-control'}),
            'profession_pere'  :   forms.TextInput(attrs={'class':'form-control'}),
            'nom_de_la_mere'  :   forms.TextInput(attrs={'class':'form-control'}),
            'profession_mere'  :   forms.TextInput(attrs={'class':'form-control'}),
            'nom_du_correspondant'  :   forms.TextInput(attrs={'class':'form-control'}),
            'adresse_des_parents'  :   forms.TextInput(attrs={'class':'form-control'}),
            'profession_correspondant'  :   forms.TextInput(attrs={'class':'form-control'}),
            'adresse_des_correspondant'  :   forms.TextInput(attrs={'class':'form-control'}),
            'sport_preferer'  :   forms.TextInput(attrs={'class':'form-control'}),
            'sport_pratique'  :   forms.TextInput(attrs={'class':'form-control'}),
            'nombre_de_frere'  :   forms.TextInput(attrs={'class':'form-control'}),
            'nombre_de_soeur'  :   forms.TextInput(attrs={'class':'form-control'}),
            'rang_dans_la_famille'  :   forms.TextInput(attrs={'class':'form-control'}),
            
        }
        labels={
            'sexe' :'Sexe',
            'position':'Position',
            'telephone':'Telephone',
            
            'email':'Email',
            'nom_du_pere':'Père',
            'profession_pere':'Profession',
            'nom_de_la_mere':'Mère',
            'profession_mere':'Profession',
            'nom_du_correspondant':'Correspondant',
            'adresse_des_parents':'Adresse des Parents',
            'profession_correspondant':'Profession',
            'adresse_des_correspondant':'Adresse Correspondant',
            'sport_preferer':'Sport Préféré',
            'sport_pratique':'Sport Pratiqué',
            'nombre_de_frere':'Nombre de Frère',
            'nombre_de_soeur':'Soeur',
            'rang_dans_la_famille':'Rang dans la famille',
            }
        
class PeriodeForm(forms.ModelForm):
    codeP = forms.CharField(label='Code Période :',widget = forms.TextInput(attrs={'class':'form-control'}))
    periode = forms.CharField(label='Période :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Periode
        fields = ['codeP','periode']
        
class PeriodeForm1(forms.ModelForm):
    # codeP = forms.CharField(label='Code Période :',widget = forms.TextInput(attrs={'class':'form-control'}))
    periode = forms.CharField(label='Période :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Periode
        fields = ['periode']
        
class AnneeScoForm(forms.ModelForm):
    codeAS = forms.CharField(label='Code Année Scolaire :',widget = forms.TextInput(attrs={'class':'form-control'}))
    annee_scolaire = forms.CharField(label='Année Scolaire :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = AnneeScolaire
        fields = ['codeAS','annee_scolaire']
        
class AnneeScoForm1(forms.ModelForm):
    # codeAS = forms.CharField(label='Code Année Scolaire :',widget = forms.TextInput(attrs={'class':'form-control'}))
    annee_scolaire = forms.CharField(label='Année Scolaire :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = AnneeScolaire
        fields = ['annee_scolaire']
        
        
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
        
class TypeFormationForm1(forms.ModelForm):
    # codeTF = forms.CharField(label='Code Type Formation :',widget = forms.TextInput(attrs={'class':'form-control'}))
    type_formation = forms.CharField(label='Type Formation :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = TypeFormation
        fields= ['type_formation']
        
        
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
        fields=['DS1','DS2','exam','observation']
        widgets = {
            'DS1'  :   forms.NumberInput(attrs={'class':'form-control','min':'0' ,'max':'20'}),
            'DS2'  :   forms.NumberInput(attrs={'class':'form-control','min':'0' ,'max':'20'}),
            'exam'  :   forms.NumberInput(attrs={'class':'form-control','min':'0' ,'max':'20'}),
            'observation': forms.TextInput(attrs={'class':'form-control'})
        }
        labels={'DS1'  :'DS1',
                'DS2':'DS2',
                'exam':'Exam',
                'observation': 'Observation'
                }

class MatForm(forms.ModelForm):
    matier = forms.CharField(label='Matière :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Matier
        fields=['matier','type_matiere']  
        widgets = {
            'type_matiere'  :   forms.Select(attrs={'class':'form-control'}),
        }
        labels={'type_matiere'  :'Type Matiere'
                }
        
class AbsForm(forms.ModelForm):
    nb_abscence = forms.CharField(label='Nombres heures d\'absence :',widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Abs
        fields=['nb_abscence']