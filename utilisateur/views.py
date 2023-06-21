from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from django.contrib import messages
from utilisateur.forms import InscriptionForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import  Permission
from django.contrib.admin.views.decorators import staff_member_required
from utilisateur.models import Utilisateur
# Create your views here.


def connexionView(request):
    if request.method == 'POST':
        utilisateur = request.POST.get('user')
        motdepasse = request.POST.get('password')
        user = authenticate(username=utilisateur,password=motdepasse)
        if user:
            login(request,user)
            request.session['user_id'] = user.id # stockage de l'ID de l'utilisateur dans la session
            request.session.save() # sauvegarde de la session avec le préfixe unique
            if request.user.is_staff:
                return redirect('index')
            else:
                return redirect('note')
        else:
            messages.error(request,"Veuillez vérifier votre nom d'utilisateur et votre mot de passe")
        
    return render(request, 'auth/connexion.html')


@staff_member_required(login_url="erreur")
# @login_required(login_url='connexion')
def inscriptionView(request):
    # permissions=Permission.objects.all()
    form = InscriptionForm()
    if request.method == "POST":
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Enregistrement succes")
            return redirect('index')
        else:
            messages.error(request,"Verifier les champs")      
    return render(request,'auth/inscrire.html',{'form': form} )


@login_required(login_url='connexion')
def profile(request):
    
    return render(request,'auth/profile.html')

@staff_member_required(login_url="erreur")
def listeUtilisateur(request):
    utilisateurs=Utilisateur.objects.all()
    return render(request,'auth/liste.html',{'utilisateurs':utilisateurs})
