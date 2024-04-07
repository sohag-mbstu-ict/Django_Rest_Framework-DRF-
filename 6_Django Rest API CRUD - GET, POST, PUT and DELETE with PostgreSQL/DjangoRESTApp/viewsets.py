from rest_framework import viewsets
from .models import Admission
from .serializers import AdmissionSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class AdmissionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AdmissionSerializer
    queryset = Admission.objects.all()

