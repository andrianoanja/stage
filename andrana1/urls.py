"""andrana1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from andrana1 import settings
from django.conf.urls.static import static
from utilisateur.views import connexionView,inscriptionView, profile
from web import views
from django.contrib.auth import views as auth_views
from utilisateur.forms import PasswordChangeForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.test,name="index"),
    path('connexion/',connexionView,name="connexion"),
    path('deconnecter/', auth_views.LogoutView.as_view(next_page='connexion'), name="deconnexion"),
    path('inscription/',inscriptionView,name="inscire"),
    path('accounts/password-change/', auth_views.PasswordChangeView.as_view(template_name='auth/changer-mdp.html', form_class=PasswordChangeForm, success_url='password-change-done'), name="password-change"),
    path('accounts/password-change/password-change-done', auth_views.PasswordChangeDoneView.as_view(template_name='auth/mdpmodif.html'), name="password-change-done"),
    path('profile/',profile,name="profile"),
    #--------------ajout---------------------------------
    path('ajoutsect',views.ajouterSect,name='ajoutsect'),
    path('ajoutfiliere',views.ajouterF,name='ajoutF'),
    path('ajoutannee',views.ajouterAnnee,name='ajoutAS'),
    path('ajoutniveau',views.ajouterN,name='ajoutN'),
    path('ajoutetudiant',views.ajouterE,name='ajoutE'),
    path('ajoutperiode',views.ajouterP,name='ajoutP'),
    path('ajouttypematiere',views.ajouterTM,name='ajoutTM'),
    path('ajoutmatiere',views.ajouterM,name='ajoutM'),
    path('ajouttypeformation',views.ajouterTF,name='ajoutTF'),
    path('ajoutmat',views.ajoutM,name='ajoutMat'),
    #-----------------afficher-------------------------
    path('afficheetudiant',views.afficheEtudiant,name='affE'),
    path('affiMat',views.affiM,name='affMat'),
    path('affichesecteur',views.afficheSect,name='affSect'),
    path('affichefiliere',views.afficheFiliere,name='affF'),
    path('afficheanneesco',views.afficheAnneeSco,name='affAS'),
    path('affichpro',views.affichePromotion,name='affPr'),
    path('afficheperiode',views.affichePeriode,name='affP'),
    path('affichetypematiere',views.afficheTypeM,name='affTM'),
    path('affichematiere',views.afficheMatiere,name='affM'),
    path('affichetypeformation',views.afficheformation,name='affTF'),
    #-----------------Modifier-------------------------
    path('modifierSecteur?id=<str:myid>',views.modifSecteur ,name='modifsecteur'),
    path('modifierfiliere?id=<str:myid>',views.modifFiliere ,name='modiffiliere'),
    path('modifierannee?id=<str:myid>',views.modifAnnee ,name='modifannee'),
    
    path('note/',views.fichenote,name="note"),
    path('ajouterFN/',views.ajoutFN,name="ficheN"),
    path('ajouterFicheN/',views.ajoutFN1,name="fichNoty"),
    path('ajoutnote?id=<int:myid>',views.ajoutN ,name='ajN'),
    path('modifNote?id=<int:id>/id=<int:myid>',views.modifierNote ,name='modifN'),
    path('bull/',views.bull,name="bull"),
    path('bul/',views.getbull,name="bul"),
    path('bulle/',views.bulle,name="bulle"),
    path('bulletin/',views.bulletin,name="bulletin"),
    path('etudS/',views.getet,name="sansM"),
    path('getetudiant/',views.getetudiant,name="getE"),
    path('etudiantM/',views.ajoutETM,name="etu"),
    path('abs/',views.absence,name="abs"),
    path('classe/',views.classe,name="classe"),
    path('bulpdf/',views.pdfbulletin,name="pdf-bul")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)