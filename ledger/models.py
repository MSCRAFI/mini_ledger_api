from django.conf import settings
from django.db import models

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customers")
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class LedgerEntry(models.Model):
    TRANSACTION_TYPES = (
        ('credit', 'Credit (Owes Money)'),
        ('debit', 'Debit (Payment Received)'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="entries")
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.TextField()
    entry_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Ledger Entries'
        ordering = ['-entry_date']

