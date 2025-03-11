from django.db import models

# Create your models here.

class Commande(models.Model):
    code = models.CharField(max_length=10,primary_key=True)
    libelle = models.CharField(max_length=15, null=False)

    def __str__(self):      
        return self.libelle


class Clients(models.Model):
    numero = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=50, null=False)
    postnom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50,null=False)
    sexe = models.CharField(max_length=1,null=False)
    adresse = models.CharField(max_length=100,null=False)
    telephone = models.CharField(max_length=15,null=False)
    e_mail = models.CharField(max_length=50,null=False)
    commande = models.ForeignKey(Commande,on_delete=models.CASCADE)