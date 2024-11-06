from rest_framework import viewsets , mixins
from .models import Medication, RefillRequest
from .serializers import MedicationSerializer, RefillRequestSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class MedicationViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Medication.objects.all().get_innotate_quantity_medication()
    serializer_class = MedicationSerializer


class RefillRequestViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = RefillRequest.objects.all()
    serializer_class = RefillRequestSerializer


    