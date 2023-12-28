from django.contrib import admin
from .models import Landlord, Apartment, Tenant, RentalContract, MaintenanceRequest, Image
# Register your models here.

@admin.register(Landlord)
class LandlordAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "updated_at")
    search_fields = ("name", )
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("address", "num_rooms", "monthly_rent", "landlord", "created_at", "updated_at")
    search_fields = ("address", )
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "updated_at")
    search_fields = ("name", )
@admin.register(RentalContract)
class RentalContract(admin.ModelAdmin):
    list_display = ("start_date", "end_date", "monthly_rent", "apartment", "tenant", "created_at", "updated_at")
    search_fields = ("start_date", )
@admin.register(MaintenanceRequest)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("description", "request_date", "is_resolved", "apartment", "created_at", "updated_at")
    search_fields = ("description", )
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image", "apartment", "created_at", "updated_at")
    search_fields = ("image", )

