from django.contrib import admin

from web.models import *

# Register your models here.
admin.site.register(Secteur)
admin.site.register(Filiere)
admin.site.register(Classe)
# admin.site.register(Etudiant)
admin.site.register(AnneeScolaire)
admin.site.register(Periode)
admin.site.register(TypeMatiere)
admin.site.register(Matiere)
admin.site.register(Matier)
admin.site.register(Note)
admin.site.register(TypeFormation)
admin.site.register(Abs)
# admin.site.register(Contenir)


@admin.register(Contenir)
class ContenirAdmin(admin.ModelAdmin):
    '''Admin View for Contenir'''

    list_display = ('etudiant','DS1','DS2','exam','DS','moyenne_par_matiere','note_avec_coeff','obs')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    '''Admin View for Etudiant'''
    list_display = ('matricule','numero','nom','prenom','classe')
