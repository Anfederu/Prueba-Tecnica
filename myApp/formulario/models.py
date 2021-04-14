from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Formulario(models.Model):
    PC_BRAND_CHOICES = (
      (1, 'HUAWEI'),
      (2, 'HP'),
      (3, 'LENOVO'),
      (4, 'ASUS'),
      (5, 'MAC'),

    )
    marca = models.PositiveSmallIntegerField(choices=PC_BRAND_CHOICES, blank=True, null=True)
    email = models.CharField(max_length=100)
    comentarios =  models.CharField(max_length=1000)
    numeroDocumento = models.IntegerField()
    fecha = models.IntegerField(default=None, blank=True, null=True)
    