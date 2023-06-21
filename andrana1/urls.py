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
from utilisateur.views import connexionView,inscriptionView, listeUtilisateur, profile
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
    path('Utilisateur/',listeUtilisateur,name="utlisateur"),
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
    path('ajoutres',views.ajouterRes,name="ajoutRes"),
    path('ajoutprov',views.ajoutProv,name="ajoutProv"),
    path('ajoutcenseur',views.ajoutCenseur,name="ajoutCenseur"),
    path('ajoutchef',views.ajoutChef,name="ajoutChef"),
    path('ajoutsg',views.ajoutSg,name="ajoutSg"),
    #-----------------afficher-------------------------
    path('afficheresp',views.afficheRes,name='affResp'),
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
    path('afficheprov',views.afficheprov,name='affprov'),
    path('affichecenseur',views.affichecenseur,name='affcenseur'),
    path('affichechef',views.afficheChef,name='affchef'),
    path('affichesg',views.afficheSg,name='affsg'),
    #-----------------Modifier-------------------------
    path('modifierSecteur?id=<str:myid>',views.modifSecteur ,name='modifsecteur'),
    path('modifierfiliere?id=<str:myid>',views.modifFiliere ,name='modiffiliere'),
    path('modifierannee?id=<str:myid>',views.modifAnnee ,name='modifannee'),
    path('modifierperiode?id=<str:myid>',views.modifPeriode ,name='modifperiode'),
    path('modifiertypematiere?id=<int:myid>',views.modifTypeM ,name='modiftypem'),
    path('modifiertypeformation?id=<str:myid>',views.modifTypeF ,name='modiftypef'),
    path('modifiermatier?id=<int:myid>/',views.modifMatiere ,name='modifmatier'),
    path('modifiermatierecoef?id=<int:myid>/',views.modifMatiereC ,name='modifmatiere'),
    path('modifierresponsableclasse?id=<int:myid>/',views.modifResponsable ,name='modifresp'),
    path('modifierclasse?id=<str:myid>/',views.modifClasse ,name='modifclasse'),
    path('modifierapprenant?id=<int:myid>/',views.modifApprenant ,name='modifapprenant'),
    path('modifierabsence?id=<int:myid>/classe=<str:id>/periode=<str:periode>/',views.modifAss ,name='modifass'),
    path('modifierproviseur?id=<int:myid>/',views.modifProv ,name='modifprov'),
    path('modifiercenseur?id=<int:myid>/',views.modifCenseur ,name='modifcenseur'),
    path('modifierchefdetravaux?id=<int:myid>/',views.modifChef ,name='modifchef'),
    path('modifiersg?id=<int:myid>/',views.modifSurveillantG ,name='modifsg'),
    
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
    path('etudS1/',views.getet1,name="sansM1"),
    path('getetudiant/',views.getetudiant,name="getE"),
    path('etudiantM/',views.ajoutETM,name="etu"),
    path('abs/',views.absence,name="abs"),
    path('classe/',views.classe,name="classe"),
    path('bulpdf/',views.pdfbulletin,name="pdf-bul"),
    path('classeapren/',views.listeparclasse,name="classapr"),
    path('classeapren1/',views.listeparclasse1,name="classapr1"),
    path('classeapren2/',views.listeparclasse2,name="classapr2"),
    path('apprenant?id=<int:myid>',views.detailEt ,name='detail'),
    path('liste/',views.listePDF,name="liste"),
    path('bulletin_annuelle/',views.bullannuelle,name="bullann"),
    path('bulletin_annuelle1/',views.bullannuelle1,name="bullann1"),
    path('bulletin_annuelle2/',views.bullannuelle2,name="bullann2"),
    path('bulletin_annuelle3/',views.bullannuelle3,name="bullann3"),
    path('fiche_ren/',views.fiche_ren,name="fiche_ren"),
    path('fiche_ren1/',views.fiche_ren1,name="fiche_ren1"),
    path('erreur/',views.erreur,name="erreur"),
    path('certificat/',views.certificat,name="certificat"),
    path('certificat1/',views.certificat1,name="certificat1"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)