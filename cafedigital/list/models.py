from django.db import models
import uuid


class Cafés(models.Model):
  SETOR_CHOICES = [
    ('hospital', 'Hospital'), ('hotel', 'Hotel'), ('hibrido', 'Híbrido'),
    ('lajes_corporativas', 'Lajes Corporativas'), 
    ('logistica', 'Logística'), ('outros', 'Outros'), 
    ('residencial', 'Residencial'),
    ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.')
  ]

  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    null=False,
    blank=True)

  codigo = models.CharField(
    max_length=8,
    null=False,
    blank=False)

  setor = models.CharField(
    max_length=30,
    null=False,
    blank=False,
    choices=SETOR_CHOICES)
