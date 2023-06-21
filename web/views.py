from django.http import HttpResponse
from django.shortcuts import render,redirect
from web.models import *
from web.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
import datetime
from django.template.loader import get_template
from xhtml2pdf import pisa
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# Create your views here.
# @staff_member_required(login_url="connexion")

@login_required(login_url='connexion')    
def test(request):
    etudiants=Etudiant.objects.all().count()
    matieres=Matier.objects.all().count()
    clas=Classe.objects.all().count()
    filieres=Filiere.objects.all().count()
    
    try:
        annee=AnneeScolaire.objects.all().last()
        classes = Classe.objects.filter(annee_scolaire=annee)

        nb_etudiants_par_classe = {}
        for f in classes:
            nb_etudiants_par_classe[f.codeC] = len(Etudiant.objects.filter(classe_id=f.codeC))
        # Créer le graphique en barres
        fig, ax = plt.subplots(figsize=(15,5))
        ax.bar(nb_etudiants_par_classe.keys(), nb_etudiants_par_classe.values(),color='#00ffff')

        fig2, ax2 = plt.subplots(figsize=(15,5))
        labels = nb_etudiants_par_classe.keys()
        values = nb_etudiants_par_classe.values()

        ax2.pie(values, labels=labels, autopct='%1.2f%%')
        ax2.axis('equal')
        ax2.set_title('Nombre d\'apprenants par  Classe' + " "+str(annee))
        ax2.legend(title='Classe', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
        plt.tight_layout()
        # Configurer le graphique
        ax.set_xlabel('Classe')
        ax.set_ylabel('Nombre d\'apprenants')
        ax.set_title('Nombre d\'apprenants par Classe' + " "+str(annee)) 

        # Convertir le graphique en image et l'afficher dans la page
        
        buffer = BytesIO()
        buffer2 = BytesIO()
        fig.savefig(buffer, format='png')
        fig2.savefig(buffer2, format='png')
        buffer.seek(0)
        buffer2.seek(0)
        image_png = buffer.getvalue()
        image_png1 = buffer2.getvalue()
        buffer.close()
        buffer2.close()
        graphic = base64.b64encode(image_png)
        graphic1 = base64.b64encode(image_png1)
        graphic = graphic.decode('utf-8')
        graphic1 = graphic1.decode('utf-8')
        return render(request,'index.html', {'etudiants':etudiants,'graphic':graphic,'matieres':matieres,'promotions':clas,'filieres':filieres,'graphic1':graphic1})
    except:
        pass
    return render(request,'index.html',{'etudiants':etudiants,'matieres':matieres,'promotions':clas,'filieres':filieres})

#----------------------ajouter------------------------------------------------
@staff_member_required(login_url="erreur")
def ajouterSect(request):
    titre="AJOUTER SECTEUR"
    form = SecteurForm()
    if request.method == "POST":
        form = SecteurForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
        else:
            messages.error(request, "Verifier les champs")
        return redirect('affSect')      
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajouterF(request):
    titre="AJOUTER FILIERE"
    form = FiliereForm()
    if request.method == "POST":
        form = FiliereForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
        else:
            messages.error(request, "Verifier les champs")
        return redirect('affF')      
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@login_required(login_url='connexion') 
def ajouterAnnee(request):
    titre="AJOUTER ANNEE SCOLAIRE"
    form = AnneeScoForm()
    if request.method == "POST":
        form = AnneeScoForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
        else:
            messages.error(request, "Verifier les champs")
        return redirect('affAS')      
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajouterRes(request):
    titre="AJOUTER RESPONSABLE DE LA CLASSE"
    form = ResponsableForm()
    if request.method == "POST":
        form = ResponsableForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
        else:
            messages.error(request, "Verifier les champs")
        return redirect('affResp')      
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajouterN(request):
    titre="AJOUTER CLASSE"
    annee=AnneeScolaire.objects.all().last()
    anne=AnneeScolaire.objects.all().last().codeAS
    form = ClasseForm()
    if request.method == "POST":
        codec=request.POST.get('codeC')
        filiere=request.POST.get('filiere')
        niveau=request.POST.get('niveau')
        typef=request.POST.get('type_formation')
        classe=request.POST.get('classe')
        resp=request.POST.get('responsable')
        try:
            query=Classe.objects.create(codeC=codec,filiere_id=filiere,niveau=niveau,type_formation_id=typef,classe=classe,annee_scolaire_id=anne,responsable_id=resp)
            messages.success(request, "Enregistrement succes")
        except:
            # query=Classe.objects.create(codeC=codec,filiere_id=filiere,niveau=niveau,type_formation_id=typef,classe=classe,annee_scolaire_id=anne,responsable_id=resp)
            messages.error(request, "Verifier les champs")
        return redirect('affPr')      
    return render(request,'ajouter/classe.html',{'form': form,'titre':titre,'annee':annee} )

@staff_member_required(login_url="erreur")
def ajouterTF(request):
    titre="AJOUTER TYPE FORMATION"
    form = TypeFormationForm()
    if request.method == "POST":
        form = TypeFormationForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
        else:
            messages.error(request, "Verifier les champs")
        return redirect('affTF')      
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def getet(request):
    titre="AJOUTER APPRENANT SANS MATRICULE"
    # aaa=AnneeScolaire.objects.all().last()
    # aa=Classe.objects.filter(annee_scolaire_id=aaa)
    typef=TypeFormation.objects.all()
    return render(request,'getet.html',{'typef':typef,'titre':titre})

@staff_member_required(login_url="erreur")
def getet1(request):
    titre="AJOUTER APPRENANT SANS MATRICULE"
    typef=request.GET['typef']
    aaa=AnneeScolaire.objects.all().last()
    aa=Classe.objects.filter(annee_scolaire_id=aaa,type_formation_id=typef)
    
    return render(request,'getet1.html',{'aa':aa,'typef':typef,'titre':titre})


@staff_member_required(login_url="erreur")
def ajouterE(request):
    titre="AJOUTER APPRENANT SANS MATRICULE"
    form = EtudiantForm()
    classe=request.GET.get('classe')
    type_formation=request.GET.get('type')
    
    count = Etudiant.objects.filter(classe__type_formation_id=type_formation)
    etudiants=[i for i in count]
    matric=[]
    maxa=1
    if etudiants:
        
        for i in etudiants:
            matri=i.matricule
            matric.append((matri))
            maxa=max(matric)+1
    b=Etudiant.objects.filter(classe=classe) 
    etu=[y for y in b]
    numero=[]
    num=1
    if etu:
        for y in etu:
            nume=y.numero
            numero.append((nume))  
            num=max(numero)+1
    if request.method  == 'POST':
        # matr=request.POST.get('matricule')
        position=request.POST.get('position')
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        photo=request.FILES['image']
        daten=request.POST.get('date_de_naissance')
        sexe=request.POST.get('sexe')
        adresse=request.POST['adresse']
        ecole_origine=request.POST['ecole_origine']
        
        tel=request.POST['telephone'] or None
        email=request.POST['email'] or None
        nom_du_pere=request.POST['nom_du_pere'] or None
        profession_pere=request.POST['profession_pere'] or None
        nom_de_la_mere=request.POST['nom_de_la_mere'] or None
        profession_mere=request.POST['profession_mere'] or None
        nom_du_correspondant=request.POST['nom_du_correspondant'] or None
        adresse_des_parents=request.POST['adresse_des_parents'] or None
        profession_correspondant=request.POST['profession_correspondant'] or None
        adresse_des_correspondant=request.POST['adresse_des_correspondant'] or None
        sport_preferer=request.POST['sport_preferer'] or None
        sport_pratique=request.POST['sport_pratique'] or None
        nombre_de_frere=request.POST['nombre_de_frere'] or None
        nombre_de_soeur=request.POST['nombre_de_soeur'] or None
        rang_dans_la_famille=request.POST['rang_dans_la_famille'] or None
    
        try:
            etudiant=Etudiant.objects.create(matricule=maxa,
                                             numero=num,
                                             nom=nom,
                                             prenom=prenom,
                                             classe_id=classe,
                                             date_de_naissance=daten,
                                             sexe=sexe,image=photo,
                                             position=position,
                                             adresse=adresse,
                                             ecole_origine=ecole_origine,
                                             telephone=tel,
                                             email=email,
                                             nom_du_pere=nom_du_pere,
                                             profession_pere=profession_pere,
                                             nom_de_la_mere=nom_de_la_mere,
                                             profession_mere=profession_mere,
                                             nom_du_correspondant=nom_du_correspondant,
                                             adresse_des_parents=adresse_des_parents,
                                             profession_correspondant=profession_correspondant,
                                             adresse_des_correspondant=adresse_des_correspondant,
                                             sport_preferer=sport_preferer,
                                             sport_pratique=sport_pratique,
                                             nombre_de_frere=nombre_de_frere,
                                             nombre_de_soeur=nombre_de_soeur,
                                             rang_dans_la_famille=rang_dans_la_famille
                                             
                                             )
            messages.success(request, "Enregistrement succes avec  numero dans la classe :"+" "+ str(num) +" "+"et matricule:"+" "+str(maxa))
        except:
            etudiant=Etudiant.objects.create(matricule=maxa,numero=num,nom=nom,prenom=prenom,classe_id=classe,date_de_naissance=daten,sexe=sexe,image=photo,position=position)
            messages.success(request, "Enregistrement succes avec  numero dans la classe :"+" "+ str(num) +" "+"et matricule:"+" "+str(maxa))

        return redirect('affE')
    return render(request,'ajouter/etudiant.html',{'form': form,'titre':titre,'b':b,'count':maxa,'num':num})

@staff_member_required(login_url="erreur") 
def getetudiant(request):
    aaa=AnneeScolaire.objects.all().last()
    aa=Classe.objects.filter(annee_scolaire_id=aaa)
    return render(request,'getetudiant.html',{'aa':aa})

@staff_member_required(login_url="erreur")
def ajoutETM(request):
    matri=request.GET.get('matricule')
    ancienC=request.GET.get('classeA')
    classe=request.GET.get('classe')
    et=Etudiant.objects.filter(classe=classe)
    etu=[y for y in et]
    numero=[]
    num=1
    if etu:
        for y in etu:
            nume=y.numero
            numero.append((nume))  
            num=max(numero)+1
    etudiant=Etudiant.objects.filter(matricule=matri,classe__classe=ancienC)
    if request.method  == 'POST':
        photo=request.FILES['image']
        position=request.POST.get('position')
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        id_niveau=request.POST.get('niveau')
        daten=request.POST.get('date_de_naissance')
        sex=request.POST.get('sexe')
        
        adresse=request.POST['adresse']
        ecole_origine=request.POST['ecole_origine']
        
        tel=request.POST['telephone'] or None
        email=request.POST['email'] or None
        nom_du_pere=request.POST['nom_du_pere'] or None
        profession_pere=request.POST['profession_pere'] or None
        nom_de_la_mere=request.POST['nom_de_la_mere'] or None
        profession_mere=request.POST['profession_mere'] or None
        nom_du_correspondant=request.POST['nom_du_correspondant'] or None
        adresse_des_parents=request.POST['adresse_des_parents'] or None
        profession_correspondant=request.POST['profession_correspondant'] or None
        adresse_des_correspondant=request.POST['adresse_des_correspondant'] or None
        sport_preferer=request.POST['sport_preferer'] or None
        sport_pratique=request.POST['sport_pratique'] or None
        nombre_de_frere=request.POST['nombre_de_frere'] or None
        nombre_de_soeur=request.POST['nombre_de_soeur'] or None
        rang_dans_la_famille=request.POST['rang_dans_la_famille'] or None
        try:
            etudiant=Etudiant.objects.create(matricule=matri,numero=num,nom=nom,prenom=prenom,classe_id=id_niveau,date_de_naissance=daten,sexe=sex,image=photo,position=position,
                                             adresse=adresse,
                                             ecole_origine=ecole_origine,
                                             telephone=tel,
                                             email=email,
                                             nom_du_pere=nom_du_pere,
                                             profession_pere=profession_pere,
                                             nom_de_la_mere=nom_de_la_mere,
                                             profession_mere=profession_mere,
                                             nom_du_correspondant=nom_du_correspondant,
                                             adresse_des_parents=adresse_des_parents,
                                             profession_correspondant=profession_correspondant,
                                             adresse_des_correspondant=adresse_des_correspondant,
                                             sport_preferer=sport_preferer,
                                             sport_pratique=sport_pratique,
                                             nombre_de_frere=nombre_de_frere,
                                             nombre_de_soeur=nombre_de_soeur,
                                             rang_dans_la_famille=rang_dans_la_famille
                                             )
            messages.success(request, "Enregistrement succes avec nouveau numero dans la classe est"+" "+ str(num))
        except:
            
            messages.error(request, "erreur")
        return redirect('affE')
    return render(request,'etudiantM.html',{'etudiant':etudiant,'aa':classe,'et':et,'num':num})



@staff_member_required(login_url="erreur")
def ajouterP(request):
    titre="AJOUTER PERIODE"
    form = PeriodeForm()
    if request.method == "POST":
        form = PeriodeForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
        else:
            messages.error(request, "Verifier les champs")
        return redirect('affP')      
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur") 
def ajouterTM(request):
    titre="AJOUTER TYPE MATIERE"
    form = TypeMatiereForm()
    if request.method == "POST":
        form = TypeMatiereForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
        else:
            messages.error(request, "Verifier les champs")
        return redirect('affTM')      
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur") 
def ajouterM(request):
    titre="AJOUTER COEFFICIENT MATIERE"
    form = MatiereForm()
    if request.method == "POST":
        form = MatiereForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
           return redirect('affM')
        else:
            messages.error(request, "Verifier les champs")
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajoutM(request):
    titre="AJOUTER MATIERE"
    form = MatForm()
    if request.method == "POST":
        form = MatForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
           return redirect('affMat')
        else:
            messages.error(request, "Verifier les champs")
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajoutProv(request):
    titre="AJOUTER PROVISEUR"
    form = ProvForm()
    if request.method == "POST":
        form = ProvForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
           return redirect('affprov')
        else:
            messages.error(request, "Verifier les champs")
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajoutCenseur(request):
    titre="AJOUTER CENSEUR"
    form = CenseurForm()
    if request.method == "POST":
        form = CenseurForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
           return redirect('affcenseur')
        else:
            messages.error(request, "Verifier les champs")
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajoutSg(request):
    titre="AJOUTER SURVEILLANT GENERAL"
    form = SgForm()
    if request.method == "POST":
        form = SgForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
           return redirect('affsg')
        else:
            messages.error(request, "Verifier les champs")
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )

@staff_member_required(login_url="erreur")
def ajoutChef(request):
    titre="AJOUTER CHEF DE TRAVAUX"
    form = ChefForm()
    if request.method == "POST":
        form = ChefForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Enregistrement succes")
           return redirect('affchef')
        else:
            messages.error(request, "Verifier les champs")
    return render(request,'ajouter/ajouter.html',{'form': form,'titre':titre } )
#---------------------------------affichage--------------------------------------------

@login_required(login_url='connexion') 
def afficheEtudiant(request):
    etudiants=Etudiant.objects.all().order_by('-id')
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        etudiants=Etudiant.objects.filter(prenom__icontains=recherche)
    pagination = Paginator(etudiants, 5)
    page = request.GET.get('page')
    etudiants = pagination.get_page(page)
    try:
        annee=AnneeScolaire.objects.all().last()
        classes = Classe.objects.filter(annee_scolaire=annee)

        nb_etudiants_par_classe = {}
        for f in classes:
            nb_etudiants_par_classe[f.codeC] = len(Etudiant.objects.filter(classe_id=f.codeC))
        # Créer le graphique en barres
        fig, ax = plt.subplots(figsize=(15,5))
        ax.bar(nb_etudiants_par_classe.keys(), nb_etudiants_par_classe.values(),color='#00ffff')

        fig2, ax2 = plt.subplots(figsize=(15,5))
        labels = nb_etudiants_par_classe.keys()
        values = nb_etudiants_par_classe.values()

        ax2.pie(values, labels=labels, autopct='%1.2f%%')
        ax2.axis('equal')
        ax2.set_title('Nombre d\'apprenants par  classe' + " "+str(annee))
        ax2.legend(title='Classe', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
        plt.tight_layout()
        # Configurer le graphique
        ax.set_xlabel('Classe')
        ax.set_ylabel('Nombre d\'apprenants')
        ax.set_title('Nombre d\'apprenants par classe' + " "+str(annee)) 

        # Convertir le graphique en image et l'afficher dans la page
        
        buffer = BytesIO()
        buffer2 = BytesIO()
        fig.savefig(buffer, format='png')
        fig2.savefig(buffer2, format='png')
        buffer.seek(0)
        buffer2.seek(0)
        image_png = buffer.getvalue()
        image_png1 = buffer2.getvalue()
        buffer.close()
        buffer2.close()
        graphic = base64.b64encode(image_png)
        graphic1 = base64.b64encode(image_png1)
        graphic = graphic.decode('utf-8')
        graphic1 = graphic1.decode('utf-8')
        return render(request,'afficher/etudiant.html', {'etudiants':etudiants,'graphic':graphic,'graphic1':graphic1,'annee':annee})
    except:
        pass
    return render(request,'afficher/etudiant.html',{'etudiants':etudiants})

@login_required(login_url='connexion') 
def afficheSect(request):
    secteurs=Secteur.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        secteurs=Secteur.objects.filter(secteur__icontains=recherche)
    pagination = Paginator(secteurs, 3)
    page = request.GET.get('page')
    secteurs = pagination.get_page(page)
    return render(request,'afficher/secteur.html', {'secteurs':secteurs})

@login_required(login_url='connexion') 
def afficheRes(request):
    responsables=Responsable.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        responsables=Responsable.objects.filter(prenom__icontains=recherche)
    pagination = Paginator(responsables, 5)
    page = request.GET.get('page')
    responsables = pagination.get_page(page)
    return render(request,'afficher/responsable.html', {'responsables':responsables})

@login_required(login_url='connexion') 
def affiM(request):
    matieres=Matier.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        matieres=Matier.objects.filter(matier__icontains=recherche)
    pagination = Paginator(matieres, 5)
    page = request.GET.get('page')
    matieres = pagination.get_page(page)
    return render(request,'afficher/matieres.html', {'matieres':matieres})

@login_required(login_url='connexion') 
def afficheFiliere(request):
    filieres=Filiere.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        filieres=Filiere.objects.filter(filiere__icontains=recherche)
    pagination = Paginator(filieres, 3)
    page = request.GET.get('page')
    filieres = pagination.get_page(page)
    return render(request,'afficher/filiere.html', {'filieres':filieres})

@login_required(login_url='connexion') 
def afficheAnneeSco(request):
    annee=AnneeScolaire.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        annee=AnneeScolaire.objects.filter(annee_scolaire__icontains=recherche)
    pagination = Paginator(annee, 3)
    page = request.GET.get('page')
    annee = pagination.get_page(page)
    return render(request,'afficher/annee.html', {'annee':annee})

@login_required(login_url='connexion') 
def affichePromotion(request):
    classes=Classe.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        classes=Classe.objects.filter(promotion__icontains=recherche)
    pagination = Paginator(classes, 6)
    page = request.GET.get('page')
    classes = pagination.get_page(page)
    return render(request,'afficher/promotion.html', {'promotions':classes})

@login_required(login_url='connexion') 
def affichePeriode(request):
    periodes=Periode.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        periodes=Periode.objects.filter(periode__icontains=recherche)
    pagination = Paginator(periodes, 3)
    page = request.GET.get('page')
    periodes = pagination.get_page(page)
    return render(request,'afficher/periode.html', {'periodes':periodes})

@login_required(login_url='connexion') 
def afficheTypeM(request):
    types=TypeMatiere.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        types=Periode.objects.filter(type_matiere__icontains=recherche)
    pagination = Paginator(types, 3)
    page = request.GET.get('page')
    types = pagination.get_page(page)
    return render(request,'afficher/typematiere.html', {'types':types})

@login_required(login_url='connexion') 
def afficheMatiere(request):
    matieres=Matiere.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        matieres=Matiere.objects.filter(matiere__icontains=recherche)
    pagination = Paginator(matieres, 3)
    page = request.GET.get('page')
    matieres = pagination.get_page(page)
    return render(request,'afficher/matiere.html', {'matieres':matieres})

@login_required(login_url='connexion') 
def afficheformation(request):
    formations=TypeFormation.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        formations=Matiere.objects.filter(matiere__icontains=recherche)
    pagination = Paginator(formations, 3)
    page = request.GET.get('page')
    formations = pagination.get_page(page)
    return render(request,'afficher/typeformation.html', {'formations':formations})

@login_required(login_url='connexion') 
def afficheprov(request):
    proviseurs=Proviseur.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        proviseurs=Proviseur.objects.filter(prenom__icontains=recherche)
    pagination = Paginator(proviseurs, 5)
    page = request.GET.get('page')
    proviseurs = pagination.get_page(page)
    return render(request,'afficher/prov.html',{'proviseurs':proviseurs})

@login_required(login_url='connexion') 
def affichecenseur(request):
    censeurs=Censeur.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        censeurs=Censeur.objects.filter(prenom__icontains=recherche)
    pagination = Paginator(censeurs, 5)
    page = request.GET.get('page')
    censeurs = pagination.get_page(page)
    return render(request,'afficher/censeur.html',{'censeurs':censeurs})

@login_required(login_url='connexion') 
def afficheSg(request):
    surveillants=SG.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        surveillants=SG.objects.filter(prenom__icontains=recherche)
    pagination = Paginator(surveillants, 5)
    page = request.GET.get('page')
    surveillants = pagination.get_page(page)
    return render(request,'afficher/sg.html',{'surveillants':surveillants})

@login_required(login_url='connexion') 
def afficheChef(request):
    chefs=ChefDeTravaux.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        chefs=ChefDeTravaux.objects.filter(prenom__icontains=recherche)
    pagination = Paginator(chefs, 5)
    page = request.GET.get('page')
    chefs = pagination.get_page(page)
    return render(request,'afficher/chef.html',{'chefs':chefs})

#--------------------------------modification----------------------------------------------
@staff_member_required(login_url="erreur")
def modifSecteur(request,myid):
    titre="MODIFIER SECTEUR"
    form = Secteur.objects.get(codeSect=myid)
    form = SecteurForm1(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affSect')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifFiliere(request,myid):
    titre="MODIFIER FILIERE"
    form = Filiere.objects.get(codeF=myid)
    form = FiliereForm1(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affF')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifAnnee(request,myid):
    titre="MODIFIER ANNEE SCOLAIRE"
    form = AnneeScolaire.objects.get(codeAS=myid)
    form = AnneeScoForm1(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affAS')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifPeriode(request,myid):
    titre="MODIFIER PERIODE"
    form = Periode.objects.get(codeP=myid)
    form = PeriodeForm1(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affP')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifTypeM(request,myid):
    titre="MODIFIER TYPE MATIERE"
    form = TypeMatiere.objects.get(id=myid)
    form = TypeMatiereForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affTM')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifTypeF(request,myid):
    titre="MODIFIER TYPE FORMATION"
    form = TypeFormation.objects.get(codeTF=myid)
    form = TypeFormationForm1(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affTF')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifMatiere(request,myid):
    titre="MODIFIER MATIERE"
    form = Matier.objects.get(id=myid)
    form = MatForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affMat')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifMatiereC(request,myid):
    titre="MODIFIER COEFFICIENT MATIERE"
    form = Matiere.objects.get(id=myid)
    form = MatiereForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affM')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifResponsable(request,myid):
    titre="MODIFIER RESPONSABLE CLASSE"
    form = Responsable.objects.get(id=myid)
    form = ResponsableForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affResp')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifClasse(request,myid):
    titre="MODIFIER CLASSE"
    form = Classe.objects.get(codeC=myid)
    form = ClasseForm1(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affPr')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifApprenant(request,myid):
    titre="MODIFIER APPRENANT"
    form = Etudiant.objects.get(id=myid)
    form = EtudiantForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affE')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifAss(request,myid,id,periode):
    titre="MODIFIER ASSUIDITE"
    etudiants=Etudiant.objects.filter(classe_id=id)
    tabl=Abs.objects.filter(periode_id=periode,etudiant_id__classe_id=id)
    form = Abs.objects.get(id=myid)
    form = AbsForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return render(request,'absence.html',{'etudiants':etudiants,'tabl':tabl,'clas':id})
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifProv(request,myid):
    titre="MODIFIER PROVISEUR"
    form = Proviseur.objects.get(id=myid)
    form = ProvForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affprov')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifCenseur(request,myid):
    titre="MODIFIER CENSEUR"
    form = Censeur.objects.get(id=myid)
    form = CenseurForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affcenseur')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifChef(request,myid):
    titre="MODIFIER CHEF DE TRAVAUX"
    form = ChefDeTravaux.objects.get(id=myid)
    form = ChefForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affchef')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def modifSurveillantG(request,myid):
    titre="MODIFIER SURVEILLANT GENERAL"
    form = SG.objects.get(id=myid)
    form = SgForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affsg')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

#--------------------------------------------------------------
@login_required(login_url='connexion') 
def fichenote(request):
    titre="FICHE DE NOTES"
    user=request.user
    annee=AnneeScolaire.objects.all().last()
    if user.is_staff:
        note=Note.objects.filter(classe__annee_scolaire=annee)
    else:
        note=Note.objects.filter(classe__annee_scolaire=annee,utilisateur_id__username=user)
    return render(request,'note.html',{'note':note,'titre':titre,'annee':annee})


@staff_member_required(login_url="erreur")
def ajoutFN(request):
    titre="CREER FICHE DE NOTE"
    annee=AnneeScolaire.objects.all().last()
    ann=annee.codeAS
    prom=Classe.objects.filter(annee_scolaire_id=ann)
    return render(request,'fiche.html',{'titre':titre,'annee':annee,'prom':prom})

@staff_member_required(login_url="erreur")
def ajoutFN1(request):
    titre="CREER FICHE DE NOTE"
    anneesc=request.GET.get('annee')
    kilasy=request.GET.get('classe')
    clas=Classe.objects.filter(codeC=kilasy)
    enseignants=Utilisateur.objects.filter(is_staff=False)
    z = [t for t in clas]
    niveau=str()
    filiere=str()
    if z:
         for m in z:
             niveau=m.niveau
             filiere=m.filiere
    matieres=Matiere.objects.filter(filiere=filiere,niveau=niveau)
    periodes=Periode.objects.all()
    if request.method  == 'POST':
        periode=request.POST.get('periode')
        matiere=request.POST.get('matiere')
        enseignant=request.POST['enseignant']
        try:
            note=Note.objects.create(annee_scolaire_id=anneesc,
                                         periode_id=periode,
                                         matiere_id=matiere,
                                         classe_id=kilasy,
                                         utilisateur_id=enseignant)
        except:
            messages.error(request, "efa miexiste")
        return redirect('note')
    return render(request,'fiche1.html',{'titre':titre,'matieres':matieres,'periodes':periodes,'enseignants':enseignants})

@login_required(login_url='connexion') 
def ajoutN(request,myid):
    id = Note.objects.get(id=myid)
    cc=Contenir.objects.filter(note_id=id)
    aa=id.classe_id
    form=Contenirform()
    etudiants=Etudiant.objects.filter(classe_id=aa)
    if request.method == "POST":
        note=request.POST.get('note')
        etudiant=request.POST.get('etudiant')
        ds1=request.POST.get('DS1')
        ds2=request.POST.get('DS2') or None
        exam=request.POST.get('exam')
        try:
            donnee=Contenir.objects.create(note_id=note,etudiant_id=etudiant,DS1=ds1,DS2=ds2,exam=exam)
        except:
                message="efa miexiste"
                return render(request,'ajoutnote.html',{'form':form,'etudiants':etudiants,'cc':cc,'mess':message})
        return render(request,'ajoutnote.html',{'id':id,'form':form,'etudiants':etudiants,'cc':cc})
    return render(request,'ajoutnote.html',{'id':id,'form':form,'etudiants':etudiants,'cc':cc})

@login_required(login_url='connexion') 
def modifierNote(request,id,myid):
    titre="MODIFICATION NOTE"
    contenir = Contenir.objects.get(id=id)
    id1 = Note.objects.get(id=myid)
    aa=id1.classe_id
    etudiants=Etudiant.objects.filter(classe_id=aa)
    cc=Contenir.objects.filter(note_id=myid)
    contenir = Contenirform(request.POST or None,instance=contenir)
    if contenir.is_valid():
        contenir.save()
        return render(request,'ajoutnote.html',{'id':id1,'cc':cc,'form':contenir,'titre':titre,'etudiants':etudiants})
    context = {'form':contenir,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@staff_member_required(login_url="erreur")
def bull(request):
    titre="AFFICHER BULLETIN"
    typef=TypeFormation.objects.all()
    filiere=Filiere.objects.all()
    return render(request,'bull.html',{'titre':titre,'typef':typef,'filiere':filiere})

@staff_member_required(login_url="erreur")
def getbull(request):
    annee=request.GET.get('annee')
    typef=request.GET.get('typef')
    filiere=request.GET.get('filiere')
    classe=Classe.objects.filter(filiere_id=filiere,annee_scolaire_id__annee_scolaire=annee,type_formation_id=typef)
    return render(request,'getbulletin.html',{'classe':classe})

@staff_member_required(login_url="erreur")
def bulle(request):
    clas=request.GET.get('classe')
    etudiants=Etudiant.objects.filter(classe_id=clas)
    periode=Periode.objects.all()
    return render(request,'bulle.html',{'etudiants':etudiants,'periode':periode,'classe':clas})

@staff_member_required(login_url="erreur")
def bulletin(request):
    classe=request.GET.get('classe')
    periode=request.GET.get('periode')
    per=Periode.objects.filter(codeP=periode)
    idEt=request.GET.get('etudiant')
    klasy=Classe.objects.filter(codeC=classe)
    etudian=Etudiant.objects.filter(id=idEt,classe_id=classe)
    z = [t for t in klasy]
    if z:
         annee=str()
         for m in z:
             annee=m.annee_scolaire_id
    abs=Abs.objects.filter(etudiant_id=idEt,periode_id=periode,annee_scolaire_id=annee)
    nbet=Etudiant.objects.filter(classe_id=classe).count()
    bulletin = Contenir.objects.filter(etudiant_id=idEt,note_id__classe_id=classe,note_id__periode_id=periode)
    promotion = Classe.objects.get(codeC=classe)
    etudiants = Etudiant.objects.filter(classe_id=promotion)
    coef =int()
    tot=float()
    nb=int()
    note=float()
    moy=float()
    cp = [p for p in bulletin]
    if cp:
        for p in cp:
            temp_coef =  p.note.matiere.coeff
            temp_tot=p.note_avec_coeff()
            temp_note= p.moyenne_par_matiere()
            temp_moy=1
            coef += temp_coef
            tot += temp_tot
            nb += temp_moy
            note += temp_note
            moy=note/nb 

    if moy >= 16:
        conduite="Tres bien"
    if moy >= 14 and moy <16:
        conduite="bien"
    if moy >= 12 and moy <14:
        conduite="Assez bien"
    if moy >=9.75 and moy <12:
        conduite="Passable" 
    if moy < 9.75:
        conduite="Laisse a desirer"
    
    if  moy < 10:
        apreciation="INSUFFISANT"
    if moy >=10 and moy < 12:
        apreciation="PASSABLE"
    if moy >=12 and moy < 14:
        apreciation="TABLEAU D'HONNEUR"
    if moy >=14 and moy < 15:
        apreciation="ENCOUREGEMANT"
    if moy >=15:
        apreciation="FELICITATION"
    bulletins = Contenir.objects.filter(note__periode_id=periode,note__classe_id=classe)
    moyennes_avec_coeff = []
    for etudiant in etudiants:
        notes_etudiant = bulletins.filter(etudiant=etudiant)
        n=0
        for note_etudiant in notes_etudiant:
            ttot = note_etudiant.note_avec_coeff()
            n += ttot
        moyennes_avec_coeff.append((n))
    moyennes_avec_coeff.sort(reverse=True)
    rang=moyennes_avec_coeff.index(tot)+1 
    return render(request,'bulletin.html',{'cl':klasy,'per':per,'etudiant':etudian,'id':abs,'nbet':nbet,'bul':bulletin,'moy':moy,'coef':coef,'tot':tot,'conduite':conduite,'apreciation':apreciation,'rang':rang,'periode':periode})

@staff_member_required(login_url="erreur")
def classe(request):
    annee=AnneeScolaire.objects.all().last()
    periode=Periode.objects.all()
    classe=Classe.objects.filter(annee_scolaire_id=annee)
    return render(request,'et.html',{'classe':classe,'periode':periode,'annee':annee})

@staff_member_required(login_url="erreur")
def absence(request):
    titre="ASSUIDITE"
    periode=request.GET.get('periode')
    clas=request.GET.get('classe')
    annee=AnneeScolaire.objects.all().last()
    etudiants=Etudiant.objects.filter(classe_id=clas)
    table=Abs.objects.filter(periode_id=periode,annee_scolaire=annee,etudiant_id__classe_id=clas).order_by('etudiant_id__classe_id')
    if request.method == 'POST':
        et=request.POST.get('etudiant')
        nb=request.POST.get('nb-abs')
        try:
            donnee=Abs.objects.create(annee_scolaire=annee,
                                  periode_id=periode,
                                  etudiant_id=et,
                                 nb_abscence=nb)
            messages.error(request, "Enregistrement succes")
            
            return render(request,'absence.html',{'titre':titre,'etudiants':etudiants,'tabl':table,'clas':clas})
        except:
            messages.error(request, "ef mi existe")
            return render(request,'absence.html',{'titre':titre,'etudiants':etudiants,'tabl':table,'clas':clas})
        
    
    return render(request,'absence.html',{'titre':titre,'etudiants':etudiants,'tabl':table,'clas':clas})

@login_required(login_url='connexion')
def pdfbulletin(request):
    classe=request.GET.get('classe')
    periode=request.GET.get('periode')
    idEt=request.GET.get('etudiant')
    per=Periode.objects.filter(codeP=periode)
    klasy=Classe.objects.filter(codeC=classe)
    etudian=Etudiant.objects.filter(id=idEt,classe_id=classe)
    z = [t for t in klasy]
    annee=str()
    if z:
         for m in z:
             annee=m.annee_scolaire_id
    abs=Abs.objects.filter(etudiant_id=idEt,periode_id=periode,annee_scolaire_id=annee)
    nbet=Etudiant.objects.filter(classe_id=classe).count()
    bulletin = Contenir.objects.filter(etudiant_id=idEt,note_id__classe_id=classe,note_id__periode_id=periode)
    promotion = Classe.objects.get(codeC=classe)
    etudiants = Etudiant.objects.filter(classe_id=promotion)
    coef =int()
    tot=float()
    nb=int()
    note=float()
    moy=float()
    cp = [p for p in bulletin]
    if cp:
        for p in cp:
            temp_coef =  p.note.matiere.coeff
            temp_tot=p.note_avec_coeff()
            temp_note= p.moyenne_par_matiere()
            temp_moy=1
            coef += temp_coef
            tot += temp_tot
            nb += temp_moy
            note += temp_note
            moy=note/nb 

    if moy >= 16:
        conduite="Tres bien"
    if moy >= 14 and moy <16:
        conduite="bien"
    if moy >= 12 and moy <14:
        conduite="Assez bien"
    if moy >=9.75 and moy <12:
        conduite="Passable" 
    if moy < 9.75:
        conduite="Laisse a desirer"
    
    if  moy < 10:
        apreciation="INSUFFISANT"
    if moy >=10 and moy < 12:
        apreciation="PASSABLE"
    if moy >=12 and moy < 14:
        apreciation="TABLEAU D'HONNEUR"
    if moy >=14 and moy < 15:
        apreciation="ENCOUREGEMANT"
    if moy >=15:
        apreciation="FELICITATION"
    bulletins = Contenir.objects.filter(note__periode_id=periode,note__classe_id=classe)
    moyennes_avec_coeff = []
    for etudiant in etudiants:
        notes_etudiant = bulletins.filter(etudiant=etudiant)
        n=0
        for note_etudiant in notes_etudiant:
            ttot = note_etudiant.note_avec_coeff()
            n += ttot
        moyennes_avec_coeff.append((n))
    moyennes_avec_coeff.sort(reverse=True)
    rang=moyennes_avec_coeff.index(tot)+1
    x = datetime.datetime.now()
    sg=SG.objects.all().last()
    chef=ChefDeTravaux.objects.all().last()
    censeur=Censeur.objects.all().last()
    prov=Proviseur.objects.all().last()
    
    template_path='bulletin_pdf.html' 
    context={'per':per,'cl':klasy,'sg':sg,'chef':chef,'censeur':censeur,'prov':prov,'etudiant':etudian,'id':abs,'nbet':nbet,'bul':bulletin,'moy':moy,'coef':coef,'tot':tot,'conduite':conduite,'apreciation':apreciation,'rang':rang,'date':x}
    response=HttpResponse(content_type='application/pdf')#application/csv application/xls
    response['Content-Disposition'] = 'filename="bulletin.pdf"'
    template=get_template(template_path)
    html=template.render(context)
    pisa_status=pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse("erreur")
    
    return response

@login_required(login_url='connexion') 
def listeparclasse(request):
    return render(request,'afficher/etudiantparclasse.html')

@login_required(login_url='connexion') 
def listeparclasse1(request):
    annee=request.GET.get('annee')
    classes=Classe.objects.filter(annee_scolaire_id__annee_scolaire=annee)
    return render(request,'afficher/etudiantparclasse1.html',{'classes':classes})

@login_required(login_url='connexion') 
def listeparclasse2(request):
    classe=request.GET.get('classe')
    apprenants=Etudiant.objects.filter(classe_id=classe)
    filles=Etudiant.objects.filter(classe_id=classe,sexe="Feminin").count()
    garçons=Etudiant.objects.filter(classe_id=classe,sexe="Masculin").count()
    return render(request,'afficher/etudiantparclasse2.html',{'apprenants':apprenants,'classe':classe,'filles':filles,'garçons':garçons})

@login_required(login_url='connexion') 
def detailEt(request,myid):
    apprenant = Etudiant.objects.get(id=myid)
    return render(request,'afficher/detail.html',{'apprenant':apprenant})

@login_required(login_url='connexion') 
def listePDF(request):
    classe=request.GET.get('classe')
    apprenants=Etudiant.objects.filter(classe_id=classe)
    filles=Etudiant.objects.filter(classe_id=classe,sexe="Feminin").count()
    garçons=Etudiant.objects.filter(classe_id=classe,sexe="Masculin").count()
    template_path='liste.html'
    context={'classe':classe,'apprenants':apprenants,'filles':filles,'garçons':garçons}
    response=HttpResponse(content_type='application/pdf')#application/csv application/xls
    response['Content-Disposition'] = 'filename="liste.pdf"'
    template=get_template(template_path)
    html=template.render(context)
    pisa_status=pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse("erreur")
    
    return response
    
@staff_member_required(login_url="erreur")
def bullannuelle(request):
    typef=TypeFormation.objects.all()
    return render(request,'bullannuel.html',{'typef':typef})

@staff_member_required(login_url="erreur")
def bullannuelle1(request):
    annee=request.GET['annee']
    typ=request.GET['type_formation']
    classes=Classe.objects.filter(annee_scolaire_id__annee_scolaire=annee,type_formation_id=typ)
    return render(request,'bullannuel1.html',{'classes':classes,'annee':annee,'typef':typ})

@staff_member_required(login_url="erreur")
def bullannuelle2(request):
    classe=request.GET['classe']
    annee=request.GET['anne']
    typefo=request.GET['typefo']
    etudiants=Etudiant.objects.filter(classe_id__classe=classe)
    return render(request,'bullannuel2.html',{'etudiants':etudiants,'classe':classe,'annee':annee,'typefo':typefo})

@staff_member_required(login_url="erreur")
def bullannuelle3(request):
    classe=request.GET['classy']
    classy=Classe.objects.filter(classe=classe)
    etudiant=request.GET['etudiant']
    apprenant=Etudiant.objects.filter(id=etudiant)
    annee=request.GET['an']
    tformation=request.GET['form']
    periodes=Periode.objects.all()
    bulletin = Contenir.objects.filter(etudiant_id=etudiant,note_id__classe_id__classe=classe)
    moys=[]
    ma=float()
    nbs=int()
    b=float()
    for periode in periodes:
        bul=bulletin.filter(note__periode=periode)
        nb=int()
        note=float()
        moy=float()!=0
        a=1

        for i in bul:
            temp_note= i.moyenne_par_matiere()
            pe=i.note.periode
            temp_moy=1
            nb += temp_moy
            note += temp_note
            moy=note/nb
        if moy == False:
            pass
        else:
            b+=moy
            nbs+=a
            ma=b/nbs
            moys.append(( moy,pe))
    absenc=Abs.objects.filter(annee_scolaire_id__annee_scolaire=annee,etudiant_id=etudiant)
    absence=int()
    cp = [p for p in absenc]
    if cp:
        for p in cp:
            temp_absc =  p.nb_abscence
            absence+=temp_absc
    etu_count=Etudiant.objects.filter(classe_id__classe=classe).count()       
     
    bulletins=Contenir.objects.filter(note_id__classe_id__classe=classe)
    etudiants=Etudiant.objects.filter(classe_id__classe=classe)
    # moysAc=[]
    # for etu in etudiants:
    #     zz=etu.matricule
    #     bulles=bulletins.filter(etudiant__matricule=zz)
        
    #     moysAp=[]
    #     for per in periodes:
    #         nb1=int()
    #         a1=1
    #         b1=float()
    #         nbs1=int()
    #         ma1=float()
    #         note1=float()
    #         bulles1=bulles.filter(note__periode=per)
    #         moysA=[]
    #         for b in bulles1:
    #             temp_note1= b.moyenne_par_matiere()
    #             temp_moy1=1
    #             nb1 += temp_moy1
    #             note1 += temp_note1
    #             moy1=note1/nb1
    #         if moy1 == False:
    #             pass
    #         else:
    #             b1+=moy1
    #             nbs1+=a1
    #             ma1=b1/nbs1
    #             moysA.append((ma1))
    
    return render(request,'bullannuel3.html',{'annee':annee,'tformation':tformation,'classe':classe,'classy':classy,'apprenant':apprenant,'bulletin':bulletin,'bul':bul,'moys':moys,'nbs':ma,'absenc':absenc,'absence':absence,'etu_count':etu_count})

@staff_member_required(login_url="erreur")
def fiche_ren(request):
    types=TypeFormation.objects.all()
    return render(request,'afficher/fiche_ren.html',{'types':types})

@staff_member_required(login_url="erreur")
def fiche_ren1(request):
    typef=request.GET['type_formation']
    matr=request.GET['matricule']
    apprenant=Etudiant.objects.filter(matricule=matr,classe_id__type_formation_id=typef).last()
    return render(request,'afficher/fiche_ren1.html',{'apprenant':apprenant})

@login_required(login_url='connexion')
def erreur(request):
    return render(request,'erreur.html')

@staff_member_required(login_url="erreur")
def certificat(request):
    titre="CERTIFICAT DE SCOLARITE"
    typef=TypeFormation.objects.all()
    return render(request,'certificat.html',{'titre':titre,'typef':typef})

@staff_member_required(login_url="erreur")
def certificat1(request):
    titre="CERTIFICAT DE SCOLARITE"
    matricule=request.GET['matricule']
    typef=request.GET['typefo']
    annee=AnneeScolaire.objects.all().last()
    proviseur=Proviseur.objects.all().last
    formation=TypeFormation.objects.filter(codeTF=typef)
    apprenants=Etudiant.objects.filter(matricule=matricule,classe_id__type_formation=typef).last()
    apprenantf=Etudiant.objects.filter(matricule=matricule,classe_id__type_formation=typef).first()
    app=apprenants.id
    app1=apprenantf.id
    apprenant1=Etudiant.objects.filter(id=app1)
    apprenant=Etudiant.objects.filter(id=app)
    template_path='certificat1.html'
    context={'classe':classe,'apprenants':apprenant,'titre':titre,'formation':formation,'annee':annee,'prov':proviseur,'apprenant':apprenant1}
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="certificat.pdf"'
    template=get_template(template_path)
    html=template.render(context)
    pisa_status=pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse("erreur")
    
    return response