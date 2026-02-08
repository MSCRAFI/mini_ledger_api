from rest_framework import serializers
from django.db.models import Sum
from .models import Customer, LedgerEntry

class LedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerEntry
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    # Calculated fields that are not stored in the database
    total_credits = serializers.SerializerMethodField()
    total_debits = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ["id", "name", "phone", "address", "total_credits", "total_debits", "balance"]

    def get_total_credits(self, obj):
        total = obj.entries.filter(type="credit").aggregate(total=Sum("amount"))["total"]
        return total or 0
    
    def get_total_debits(self, obj):
        total = obj.entries.filter(type="debit").aggregate(total=Sum("amount"))["total"]
        return total or 0

    def get_balance(self, obj):
        total_credits = self.get_total_credits(obj)
        total_debits = self.get_total_debits(obj)
        return total_credits - total_debits