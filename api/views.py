from rest_framework import viewsets
from .models import Employe
from .serializers import EmployeSerializer


class EmployeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeSerializer
    queryset = Employe.objects.all()
