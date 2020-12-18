from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Employe(models.Model):
    id_employe=models.Field(primary_key=True)
    nom_employe=models.CharField(max_length=200)
    prenom_employe=models.CharField(max_length=200)
    adresse_employe=models.CharField(max_length=200)
    datenaissance_employe=models.DateField()
    email_employe=models.CharField(max_length=200)
    mdp_employe=models.CharField(max_length=200)
    role_employe=models.CharField(max_length=200)
    suppr_employe=models.IntegerField()



class Chantier(models.Model):
    id_chantier=models.Field(primary_key=True)
    adresse_chantier=models.CharField(max_length=200)
    datedeb_chantier=models.DateField()
    datefin_chantier=models.DateField()
    statut_chantier=models.CharField(max_length=200)

class asso_chant_emp(models.Model):
    id_chantier=models.ForeignKey(Chantier,on_delete=models.CASCADE)
    id_employe=models.ForeignKey(Employe,on_delete=models.CASCADE)
    date_chantier=models.DateField()
    Nbheure_chantier=models.IntegerField()
    statsuppr_chant=models.IntegerField()