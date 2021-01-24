# Create your models here.
from django.db import models


class Chantier(models.Model):
    adresse = models.CharField(max_length=200)
    datedeb = models.DateField()
    datefin = models.DateField()
    statut = models.CharField(max_length=200)

    def __str__(self):
        return self.adresse


class Employe(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    datenaissance = models.DateField()
    email = models.CharField(max_length=200)
    mdp = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    suppr = models.IntegerField()
    chantiers = models.ManyToManyField(Chantier, through="Timesheet")

    def __str__(self):
        return self.nom


class Timesheet(models.Model):
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date = models.DateField()
    nbheure = models.IntegerField()

    def get_month_format(self):
        """
        Get a month format string in strptime syntax to be used to parse the
        month from url variables.
        """
        return self.month_format

