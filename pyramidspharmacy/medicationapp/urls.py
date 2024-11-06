from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicationViewSet, RefillRequestViewSet 

router = DefaultRouter()
router.register('medications', MedicationViewSet)
router.register('refill_requests', RefillRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
