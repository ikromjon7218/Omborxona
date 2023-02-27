from django.db import models
from asosiy.models import Client, Mahsulot, Ombor

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    sana = models.DateTimeField(auto_now_add=True)
    narx = models.CharField(max_length=20)
    tolandi = models.CharField(max_length=20)
    qarz = models.CharField(max_length=20)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.mahsulot}"