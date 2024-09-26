from django.db import models

# Create your models here.
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Pays(models.Model):
    nom = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=255)  # Champ obligatoire
    description = models.TextField(blank=True, null=True)  # Facultatif
    caracteristiques_particulieres = models.TextField(blank=True, null=True)  # Facultatif
    prix_commercial = models.DecimalField(max_digits=10, decimal_places=2)  # Champ obligatoire
    prix_partenaire = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Facultatif
    couleur = models.CharField(max_length=50, blank=True, null=True)  # Facultatif
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)  # Champ obligatoire
    image = models.ImageField(upload_to='produits/', blank=False, null=False)  # Image obligatoire
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, blank=True, null=True)  # Facultatif

    def __str__(self):
        return self.nom


class Profil(models.Model):
    username = models.CharField(max_length=255)
    numero_whatsapp = models.CharField(max_length=15)

    def __str__(self):
        return self.username
