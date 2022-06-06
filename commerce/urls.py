
from django.contrib import admin
from django.urls import path
from boutique.views import index,detail_du_produit,Ajout_au_panier,Home, panier
from django.conf.urls.static import static
from commerce import settings
from compte.views import Inscrire, Connexion, Deconnecter


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('home', Home, name="home"),
     path('panier', panier, name="panier"),
    path('inscrire', Inscrire, name="inscrire"),
    path('connexion/', Connexion, name="connexion"),
    path('deconnexion/', Deconnecter, name="deconnexion"),
    path('produit/<str:slug>/', detail_du_produit,name="produit"),
    path('produit/<str:slug>/ajout_au_panier/',Ajout_au_panier,name="ajout_au_panier"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)