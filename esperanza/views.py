from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from .models import Categorie, Pays, Produit, Profil

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Categorie, Pays, Produit, Profil

def dashboard_view(request):
    if request.method == 'POST':
        # Ajout de catégorie
        categorie_nom = request.POST.get('categorie_nom')
        if categorie_nom:
            Categorie.objects.create(nom=categorie_nom)

        # Ajout de pays
        pays_nom = request.POST.get('pays_nom')
        pays_code = request.POST.get('pays_code')
        if pays_nom and pays_code:
            Pays.objects.create(nom=pays_nom, code=pays_code)

        # Ajout de produit
        produit_nom = request.POST.get('produit_nom')
        produit_description = request.POST.get('produit_description')
        produit_prix_commercial = request.POST.get('produit_prix_commercial')
        produit_prix_partenaire = request.POST.get('produit_prix_partenaire')
        produit_couleur = request.POST.get('produit_couleur')
        produit_categorie_id = request.POST.get('produit_categorie')
        produit_pays_id = request.POST.get('produit_pays')
        image = request.FILES.get('image')  # Image du produit

        if produit_nom and produit_prix_commercial and produit_categorie_id:
            # Récupérer la catégorie et le pays associés
            categorie = Categorie.objects.get(id=produit_categorie_id)
            pays = Pays.objects.get(id=produit_pays_id) if produit_pays_id else None

            # Gestion de l'image si elle est fournie
            if image:
                produit = Produit(
                    nom=produit_nom,
                    description=produit_description,
                    prix_commercial=produit_prix_commercial,
                    prix_partenaire=produit_prix_partenaire,
                    couleur=produit_couleur,
                    categorie=categorie,
                    pays=pays,
                    image=image  # Utilisation de l'image directement dans le modèle
                )
                produit.save()
            else:
                # Si pas d'image, on crée le produit sans image
                Produit.objects.create(
                    nom=produit_nom,
                    description=produit_description,
                    prix_commercial=produit_prix_commercial,
                    prix_partenaire=produit_prix_partenaire,
                    couleur=produit_couleur,
                    categorie=categorie,
                    pays=pays
                )

        # Ajout de profil
        profil_username = request.POST.get('profil_username')
        profil_whatsapp = request.POST.get('profil_whatsapp')
        if profil_username and profil_whatsapp:
            Profil.objects.create(username=profil_username, numero_whatsapp=profil_whatsapp)

        # Redirection après soumission pour éviter la soumission multiple
        return redirect('dashboard_view')

    # Obtenir toutes les données à afficher dans le dashboard
    categories = Categorie.objects.all()
    pays = Pays.objects.all()
    produits = Produit.objects.all()
    profils = Profil.objects.all()

    context = {
        'categories': categories,
        'pays': pays,
        'produits': produits,
        'profils': profils,
    }
    return render(request, 'dashboard.html', context)

from django.shortcuts import render
from .models import Produit

def produits_view(request):
    produits = Produit.objects.all().order_by('-id')  # Afficher du dernier au premier produit
    return render(request, 'produits.html', {'produits': produits})



from django.shortcuts import render, get_object_or_404
from .models import Produit

def produit_detail_view(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produits_similaires = Produit.objects.filter(categorie=produit.categorie).exclude(id=produit_id)

    context = {
        'produit': produit,
        'produits_similaires': produits_similaires,
    }
    return render(request, 'produit_detail.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Produit, Categorie

def produits_par_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    produits = Produit.objects.filter(categorie=categorie)
    
    return render(request, 'categorie_produits.html', {
        'categorie': categorie,
        'produits': produits
    })
