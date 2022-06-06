from django.db  import models
from django.urls import reverse
from commerce.settings import AUTH_USER_MODEL

class Produit (models.Model):
        nom=models.CharField( max_length=250)
        slug=models.SlugField(default="",max_length=185)
        prix=models.FloatField(default=0.0)
        stock=models.IntegerField(default=0)
        description=models.TextField(blank=True)
        photo=models.ImageField(upload_to="PRODUIT", blank=True ,null=True )
        
        def __str__(self):
          return self.nom
        def get_absolute_url(self):
            return reverse("produit", kwargs={"slug": self.slug})


             

class Article(models.Model):
  utilisateur=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
  produit=models.ForeignKey("Produit", on_delete=models.CASCADE)
  quantite=models.IntegerField(default=1)
  etat=models.BooleanField(default=False)
  def __str__(self): 
          return f"{self.produit.nom} ({self.quantite})"




class Panier (models.Model):
  utilisateur=models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
  articles=models.ManyToManyField(Article)
  reserve=models.BooleanField(default=True)
  date_article=models.DateTimeField(blank=True, null=True)
def __str__(self): 
          return self.produit.utilisateur.nom 
