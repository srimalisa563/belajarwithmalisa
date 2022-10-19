from django.db import models

# Create your models here.
class Materi(models.Model):
    judul = models.CharField(max_length=50)
    kategori = models.CharField(max_length=20)

def _str_(self):
    return self.judul