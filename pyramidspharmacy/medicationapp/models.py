from django.db import models
from django.conf import settings
from .conf import STATUS_CHOICES , PENDING
from .mixin_model import   RefillRequestMixin
from .manager import MedicationQuerySet
class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = MedicationQuerySet.as_manager()

    def __str__(self):
        return self.name



class RefillRequest(RefillRequestMixin , models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES , default=PENDING)
    approved_at = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return f'Refill request for {self.medication.name} by {self.user.username}'
