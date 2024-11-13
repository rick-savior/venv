from rest_framework import serializers
from list.models import Cafés


class CafésSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cafés
    fields = [
      'id',
      'codigo',
      'setor',

    ]