from django.db import models
from django.contrib.auth.models import User
class Ombor(models.Model):
    nom = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    manzil = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nom}"

class Mahsulot(models.Model):
    nom = models.CharField(max_length=20)
    brend = models.CharField(max_length=20)
    narx = models.CharField(max_length=30)
    kelgan_sana = models.DateField()
    miqdor = models.IntegerField()
    olchov = models.CharField(max_length=30)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}"

class Client(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    qarz = models.CharField(max_length=20)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}"