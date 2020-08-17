from django.db import models


class Employe(models.Model):
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=124)
    department = models.CharField(max_length=124)
