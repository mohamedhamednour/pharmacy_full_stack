from django.contrib import admin
from .models import Medication, RefillRequest

# Admin configuration for Medication model
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'quantity', 'created_at')  
    search_fields = ('name',) 
    list_filter = ('created_at',) 
    ordering = ('created_at',)  

# Admin configuration for RefillRequest model
class RefillRequestAdmin(admin.ModelAdmin):
    list_display = ('medication', 'user', 'status', 'approved_at') 
    search_fields = ('medication__name', 'user__username') 
    list_filter = ('status', 'approved_at') 
    ordering = ('-approved_at',) 

admin.site.register(Medication, MedicationAdmin)
admin.site.register(RefillRequest, RefillRequestAdmin)
