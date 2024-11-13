from list.serializers import CafésSerializer
from rest_framework import viewsets, permissions
from list.models import Cafés

class CafésViewSet(viewsets.ModelViewSet):
  queryset = Cafés.objects.all()
  serializer_class = CafésSerializer
  permission_classes = [permissions.IsAuthenticated]