from django.shortcuts import render
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer, LedgerEntry
from .serializers import CustomerSerializer, LedgerEntrySerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    # queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # filter so that users only see their own customers
        return Customer.objects.filter(user=self.request.user).prefetch_related('entries')
    def perform_create(self, serializer):
        # set the user field to the logged in user when creating a new customer
        serializer.save(user=self.request.user)

class LedgerEntryViewSet(viewsets.ModelViewSet):
    serializer_class = LedgerEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'customer': ['exact'],
        'type': ['exact'],
        'entry_date': ['gte', 'lte'],
    }

    def get_queryset(self):
        # filter so that users only see entries for their own customers
        print(f"Current User: {self.request.user}") # Check your terminal output
        return LedgerEntry.objects.filter(customer__user=self.request.user).select_related('customer')