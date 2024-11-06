
from django.db.models import Sum, OuterRef, Subquery , QuerySet

class MedicationQuerySet(QuerySet):

    def get_innotate_quantity_medication(self):
        from .models import RefillRequest
        return self.annotate(
            total_refill_quantity=Subquery(
                RefillRequest.objects.filter(medication=OuterRef('pk'))
                .values('medication')
                .annotate(quantity_sum=Sum('quantity'))
                .values('quantity_sum')[:1]
            )
        )