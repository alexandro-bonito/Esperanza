from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categorie, Pays, Produit, Profil

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

class PaysAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code')
    search_fields = ('nom',)

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'pays', 'prix_commercial', 'prix_partenaire', 'couleur','image')
    list_filter = ('categorie', 'pays')
    search_fields = ('nom', 'description')

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('username', 'numero_whatsapp')
    search_fields = ('username',)

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Pays, PaysAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Profil, ProfilAdmin)
