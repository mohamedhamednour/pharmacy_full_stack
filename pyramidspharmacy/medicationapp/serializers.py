from rest_framework import serializers
from .models import Medication, RefillRequest

class MedicationSerializer(serializers.ModelSerializer):
    total_refill_quantity = serializers.IntegerField()
    class Meta:
        model = Medication
        fields = ['name', 'total_refill_quantity']


class RefillRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefillRequest
        fields = ['id', 'medication', 'status', 'approved_at' , 'quantity']
