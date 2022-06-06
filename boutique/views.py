from django.shortcuts import render,get_object_or_404,redirect
from boutique.models import Produit,Panier,Article
from django.urls import reverse
from django.http import HttpResponse

def index (request):
    produits = Produit.objects.all()
    return render(request ,'boutique/index.html', context = {"produits": produits})
def Home(request):
    produits = Produit.objects.all()
    return render(request ,'header.html')


def detail_du_produit(request,slug):
    produit = get_object_or_404(Produit,slug=slug)
    return render(request ,'boutique/detail.html', context = {"produit": produit})


def Ajout_au_panier(request,slug):
    utilisateur = request.user
    produit = get_object_or_404(Produit,slug=slug)
    panier, _ = Panier.objects.get_or_create(utilisateur=utilisateur)
    article,creer = Article.objects.get_or_create(utilisateur=utilisateur, produit=produit)
    
    if creer:
        panier.articles.add(article)
        panier.save()
    else:
        article.quantite +=1
        article.save()
    return redirect(reverse("produit",kwargs={"slug": slug}))



def panier(request):
    panier = get_object_or_404 (Panier,utilisateur=request.user)
    return render(request ,'boutique/panier.html', context={"articles": panier.articles.all()})
