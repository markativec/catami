from django.db import models

# Create your models here.
class campaign(models.Model):
    description=models.CharField(max_length=200)
    associatedResearchers=models.CharField(max_length=200)
    associatedPublications=models.CharField(max_length=200)
    associatedResearchGrant=models.CharField(max_length=200)
    deployments=models.CharField(max_length=200)

class users(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    organisation=models.CharField(max_length=200)

