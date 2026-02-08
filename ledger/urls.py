from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, LedgerEntryViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'entries', LedgerEntryViewSet, basename='ledger-entry')

urlpatterns = [
    path('', include(router.urls)),
]