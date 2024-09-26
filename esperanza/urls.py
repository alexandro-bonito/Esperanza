from django.contrib import admin
from django.urls import path
from . import views  # Assurez-vous que cela est correct

urlpatterns = [

    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('', views.produits_view, name='produits'),
    path('produit/<int:produit_id>/', views.produit_detail_view, name='produit_detail'),
    path('categorie/<int:categorie_id>/', views.produits_par_categorie, name='produits_par_categorie'),

]
