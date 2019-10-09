from patients.models import Patient
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientSerializer

    def list(self, request):
        return Response([])
