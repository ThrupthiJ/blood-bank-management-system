
from django.contrib import admin
from .models import (
    DonorScreening,
    ComponentSeparation,
    ColdStorage,
    Dispatch,
)


admin.site.site_header = "BBMS | Blood Bank Management"
admin.site.site_title = "BBMS Administration"
admin.site.index_title = "Blood Bank Operations Dashboard"


@admin.register(DonorScreening)
class DonorScreeningAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "age",
        "blood_group",
        "screening_date",
        "screening_status",
    )
    list_filter = ("blood_group", "screening_status", "screening_date")
    search_fields = ("full_name", "phone")
    ordering = ("-screening_date",)


@admin.register(ComponentSeparation)
class ComponentSeparationAdmin(admin.ModelAdmin):
    list_display = (
        "batch_number",
        "donor",
        "component_type",
        "quantity_units",
        "separation_date",
    )
    list_filter = ("component_type", "separation_date")
    search_fields = ("batch_number", "donor__full_name")
    ordering = ("-separation_date",)


@admin.register(ColdStorage)
class ColdStorageAdmin(admin.ModelAdmin):
    list_display = (
        "storage_location",
        "component",
        "expiry_date",
        "available_units",
        "status",
    )
    list_filter = ("status", "expiry_date")
    search_fields = ("storage_location", "component__batch_number")
    ordering = ("expiry_date",)


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = (
        "recipient_hospital",
        "storage",
        "quantity_units",
        "dispatch_date",
        "authorized_by",
        "status",
    )
    list_filter = ("status", "dispatch_date")
    search_fields = ("recipient_hospital", "authorized_by")
    ordering = ("-dispatch_date",)
