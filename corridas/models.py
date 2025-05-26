from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as models_geo
class Motorista(models.Model):
    nome = models.CharField(max_length=255)
    localizacao = models_geo.PointField(geography=True)
    avaliacao = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    def __str__(self):
        return self.nome