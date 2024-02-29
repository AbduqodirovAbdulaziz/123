from django.db import models
from django.contrib.auth.models import User


class Bolim(models.Model):
    nomi = models.CharField(max_length=255)
    haqida = models.CharField(max_length=255)

    def __str__(self):
        return f"Nomi:{self.nomi}"


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    familiya = models.CharField(max_length=30)
    tirik = models.CharField(max_length=10, choices=[("tirik", "tirik"), ("o'lgan", "o'lgan")])
    mamlakat = models.CharField(max_length=35, blank=True, null=True)

    def __str__(self):
        return f" Muallif: {self.ism} {self.familiya}"

class Kitob(models.Model):
    nomi=models.CharField(max_length=30)
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    yili=models.DateField()
    bolim=models.ForeignKey(Bolim, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks')
    file=models.FileField(null=True,blank=True)

    def __str__(self):
        return f" Nomi: {self.nomi} Bo'lim: {self.bolim}"