from django.http import HttpResponse
from django.shortcuts import render,redirect
from web.models import *
from web.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime
from django.template.loader import get_template
from xhtml2pdf import pisa
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# Create your views here.
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
        ax2.set_title('Nombre d\'étudiants par  Classe' + " "+str(annee))
        ax2.legend(title='Classe', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
        plt.tight_layout()
        # Configurer le graphique
        ax.set_xlabel('Classe')
        ax.set_ylabel('Nombre d\'étudiants')
        ax.set_title('Nombre d\'étudiants par Classe' + " "+str(annee)) 

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
@login_required(login_url='connexion') 
def ajouterSect(request):
    titre="Ajouter Secteur"
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

@login_required(login_url='connexion') 
def ajouterF(request):
    titre="Ajouter Filière"
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
    titre="Ajouter Année Scolaire"
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

@login_required(login_url='connexion') 
def ajouterN(request):
    titre="Ajouter Classe"
    annee=AnneeScolaire.objects.all().last()
    anne=AnneeScolaire.objects.all().last().codeAS
    form = ClasseForm()
    if request.method == "POST":
        codec=request.POST.get('codeC')
        filiere=request.POST.get('filiere')
        niveau=request.POST.get('niveau')
        typef=request.POST.get('type_formation')
        classe=request.POST.get('classe')
        try:
            query=Classe.objects.create(codeC=codec,filiere_id=filiere,niveau=niveau,type_formation_id=typef,classe=classe,annee_scolaire_id=anne)
            messages.success(request, "Enregistrement succes")
        except:
            query=Classe.objects.create(codeC=codec,filiere_id=filiere,niveau=niveau,type_formation_id=typef,classe=classe,annee_scolaire_id=anne)
            messages.error(request, "Verifier les champs")
        return redirect('affPr')      
    return render(request,'ajouter/classe.html',{'form': form,'titre':titre,'annee':annee} )

@login_required(login_url='connexion') 
def ajouterTF(request):
    titre="Ajouter Type Formation"
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

@login_required(login_url='connexion') 
def getet(request):
    titre="Ajouter Etudiant Sans Matricule"
    aaa=AnneeScolaire.objects.all().last()
    aa=Classe.objects.filter(annee_scolaire_id=aaa)
    typef=TypeFormation.objects.all()
    return render(request,'getet.html',{'aa':aa,'typef':typef,'titre':titre})


@login_required(login_url='connexion') 
def ajouterE(request):
    titre="Ajouter Etudiant Sans Matricule"
    form = EtudiantForm()
    classe=request.GET.get('classe')
    type_formation=request.GET.get('typef')
    
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
        # numero=request.POST.get('numero')
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        # id_niveau=request.POST.get('classe')
        daten=request.POST.get('date_de_naissance')
        sexe=request.POST.get('sexe')
        try:
            etudiant=Etudiant.objects.create(matricule=maxa,numero=num,nom=nom,prenom=prenom,classe_id=classe,date_de_naissance=daten,sexe=sexe)
            messages.success(request, "Enregistrement succes avec  numero dans la classe :"+" "+ str(num) +" "+"et matricule:"+" "+str(maxa))
        except:
            etudiant=Etudiant.objects.create(matricule=maxa,numero=num,nom=nom,prenom=prenom,classe_id=classe,date_de_naissance=daten,sexe=sexe)
            messages.success(request, "Enregistrement succes avec  numero dans la classe :"+" "+ str(num) +" "+"et matricule:"+" "+str(maxa))

        return redirect('affE')
    return render(request,'ajouter/etudiant.html',{'form': form,'titre':titre,'b':b,'count':maxa,'num':num})

@login_required(login_url='connexion') 
def getetudiant(request):
    aaa=AnneeScolaire.objects.all().last()
    aa=Classe.objects.filter(annee_scolaire_id=aaa)
    return render(request,'getetudiant.html',{'aa':aa})

@login_required(login_url='connexion') 
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
        # matr=request.POST.get('matricule')
        # numero=request.POST.get('numero')
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        id_niveau=request.POST.get('niveau')
        daten=request.POST.get('date_de_naissance')
        sex=request.POST.get('sexe')
        try:
            etudiant=Etudiant.objects.create(matricule=matri,numero=num,nom=nom,prenom=prenom,classe_id=id_niveau,date_de_naissance=daten,sexe=sex)
            messages.success(request, "Enregistrement succes avec nouveau numero dans la classe est"+" "+ str(num))
        except:
            
            messages.error(request, "erreur")
        return redirect('affE')
    return render(request,'etudiantM.html',{'etudiant':etudiant,'aa':classe,'et':et,'num':num})



@login_required(login_url='connexion') 
def ajouterP(request):
    titre="Ajouter Periode"
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

@login_required(login_url='connexion') 
def ajouterTM(request):
    titre="Ajouter Type Matière"
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

@login_required(login_url='connexion') 
def ajouterM(request):
    titre="Ajouter coeficiant Matière"
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

@login_required(login_url='connexion') 
def ajoutM(request):
    titre="Ajouter Matière"
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
        ax2.set_title('Nombre d\'étudiants par  classe' + " "+str(annee))
        ax2.legend(title='Classe', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
        plt.tight_layout()
        # Configurer le graphique
        ax.set_xlabel('Classe')
        ax.set_ylabel('Nombre d\'étudiants')
        ax.set_title('Nombre d\'étudiants par classe' + " "+str(annee)) 

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

#--------------------------------modification----------------------------------------------
@login_required(login_url='connexion')
def modifSecteur(request,myid):
    titre="Modifier Secteur"
    form = Secteur.objects.get(codeSect=myid)
    form = SecteurForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affSect')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@login_required(login_url='connexion')
def modifFiliere(request,myid):
    titre="Modifier Filiere"
    form = Filiere.objects.get(codeF=myid)
    form = FiliereForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affF')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)

@login_required(login_url='connexion')
def modifAnnee(request,myid):
    titre="Modifier Année Scolaire"
    form = AnneeScolaire.objects.get(codeAS=myid)
    form = AnneeScoForm(request.POST or None,instance=form)
    if form.is_valid():
        form.save()
        return redirect('affAS')
    context = {'form':form,'titre':titre}
    return render(request,'ajouter/ajouter.html',context)


@login_required(login_url='connexion') 
def fichenote(request):
    titre="Fiche de notes"
    annee=AnneeScolaire.objects.all().last()
    note=Note.objects.filter(classe__annee_scolaire=annee)
    return render(request,'note.html',{'note':note,'titre':titre,'annee':annee})


@login_required(login_url='connexion') 
def ajoutFN(request):
    titre="Creer Fiche de note"
    annee=AnneeScolaire.objects.all().last()
    ann=annee.codeAS
    prom=Classe.objects.filter(annee_scolaire_id=ann)
    return render(request,'fiche.html',{'titre':titre,'annee':annee,'prom':prom})

@login_required(login_url='connexion')
def ajoutFN1(request):
    titre="Creer Fiche de note"
    anneesc=request.GET.get('annee')
    kilasy=request.GET.get('classe')
    clas=Classe.objects.filter(codeC=kilasy)
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
        try:
            note=Note.objects.create(annee_scolaire_id=anneesc,
                                         periode_id=periode,
                                         matiere_id=matiere,
                                         classe_id=kilasy)
        except:
            messages.error(request, "efa miexiste")
        return redirect('note')
    return render(request,'fiche1.html',{'titre':titre,'matieres':matieres,'periodes':periodes})

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
        ds2=request.POST.get('DS2')
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
    titre="modification Note"
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

@login_required(login_url='connexion')
def bull(request):
    titre="Afficher bulletin"
    typef=TypeFormation.objects.all()
    filiere=Filiere.objects.all()
    return render(request,'bull.html',{'titre':titre,'typef':typef,'filiere':filiere})

@login_required(login_url='connexion') 
def getbull(request):
    annee=request.GET.get('annee')
    typef=request.GET.get('typef')
    filiere=request.GET.get('filiere')
    classe=Classe.objects.filter(filiere_id=filiere,annee_scolaire_id__annee_scolaire=annee,type_formation_id=typef)
    return render(request,'getbulletin.html',{'classe':classe})

@login_required(login_url='connexion')
def bulle(request):
    clas=request.GET.get('classe')
    etudiants=Etudiant.objects.filter(classe_id=clas)
    periode=Periode.objects.all()
    return render(request,'bulle.html',{'etudiants':etudiants,'periode':periode,'classe':clas})

@login_required(login_url='connexion') 
def bulletin(request):
    classe=request.GET.get('classe')
    periode=request.GET.get('periode')
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
    
    if  moy <= 9.75:
        apreciation="INSUFFISANT"
    else:
        apreciation="TSARA"
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
    return render(request,'bulletin.html',{'cl':klasy,'etudiant':etudian,'id':abs,'nbet':nbet,'bul':bulletin,'moy':moy,'coef':coef,'tot':tot,'conduite':conduite,'apreciation':apreciation,'rang':rang,'periode':periode})

@login_required(login_url='connexion') 
def classe(request):
    annee=AnneeScolaire.objects.all().last()
    periode=Periode.objects.all()
    classe=Classe.objects.filter(annee_scolaire_id=annee)
    return render(request,'et.html',{'classe':classe,'periode':periode,'annee':annee})

@login_required(login_url='connexion') 
def absence(request):
    titre="Absence"
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
            
            return render(request,'absence.html',{'titre':titre,'etudiants':etudiants,'tabl':table})
        except:
            messages.error(request, "ef mi existe")
            return render(request,'absence.html',{'titre':titre,'etudiants':etudiants,'tabl':table})
        
    
    return render(request,'absence.html',{'titre':titre,'etudiants':etudiants,'tabl':table})

@login_required(login_url='connexion')
def pdfbulletin(request):
    classe=request.GET.get('classe')
    periode=request.GET.get('periode')
    idEt=request.GET.get('etudiant')
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
    
    if  moy <= 9.75:
        apreciation="INSUFFISANT"
    else:
        apreciation="TSARA"
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
    
    template_path='bulletin_pdf.html'
    context={'cl':klasy,'etudiant':etudian,'id':abs,'nbet':nbet,'bul':bulletin,'moy':moy,'coef':coef,'tot':tot,'conduite':conduite,'apreciation':apreciation,'rang':rang,'date':x}
    response=HttpResponse(content_type='application/pdf')#application/csv application/xls
    response['Content-Disposition'] = 'filename="bulletin.pdf"'
    template=get_template(template_path)
    html=template.render(context)
    pisa_status=pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse("erreur")
    
    return response