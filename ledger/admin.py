from django.contrib import admin
from .models import Customer, LedgerEntry

# This allows you to edit Ledger Entries inside the Customer page
class LedgerEntryInline(admin.TabularInline):
    model = LedgerEntry
    extra = 1  # Provides one empty row to quickly add a new entry
    fields = ('entry_date', 'type', 'amount', 'note')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # What to show in the main list
    list_display = ('name', 'phone', 'user', 'created_at')
    
    # Add a sidebar to filter by user or date
    list_filter = ('user', 'created_at')
    
    # Search bar for name and phone
    search_fields = ('name', 'phone')
    
    # Attach the Ledger entries to the bottom of the Customer page
    inlines = [LedgerEntryInline]

@admin.register(LedgerEntry)
class LedgerEntryAdmin(admin.ModelAdmin):
    list_display = ('customer', 'entry_date', 'type', 'amount')
    list_filter = ('type', 'entry_date', 'customer')
    search_fields = ('customer__name', 'note')
    date_hierarchy = 'entry_date' # Adds a nice date drill-down at the top