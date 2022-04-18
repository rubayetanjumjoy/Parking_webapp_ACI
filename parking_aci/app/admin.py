from django.contrib import admin
from .models import Registration
from .models import Entry
from .models import Exit
from .models import logbook
from .models import UnregisteredVehicle
from .models import History
# Register your models here.
admin.site.site_header = "ACI PARKING"
from .models import HistoryUnregistered
#/root/1234rtyu
class EntryAdmin(admin.ModelAdmin):

    search_fields = ('user__vehicle_number','user__full_name')

    list_display = (
         'user','ts_created', 'ts_updated', 'user','id'
    )


class ExitAdmin(admin.ModelAdmin):
    search_fields = ('user__vehicle_number',)

    list_display = (
         'user','ts_created', 'ts_updated', 'id'
    )


class RegiAdmin(admin.ModelAdmin):
    search_fields = ('vehicle_number',)
    list_display = (
        'stuff_id', 'full_name', 'department', 'phone_no', 'designation', 'vehicle_number',
        'vehicle_type', 'ts_created', 'ts_updated'
    )


class loogbookadmin(admin.ModelAdmin):
    list_display = (
        'user', 'status'
    )
class UnregisteredVehicleAdmin(admin.ModelAdmin):
    list_display = (
        'urnumber', 'ts_created', 'ts_updated'
    )
class historyadmin(admin.ModelAdmin):
    search_fields = ('platenumber',)
    list_display = (
        'platenumber', 'ts_created', 'ts_updated',
    )
class HistoryUnregisteredAdmin(admin.ModelAdmin):
    search_fields = ('platenumber',)
    list_display = (
        'platenumber', 'ts_created', 'ts_updated'
    )


admin.site.register(Registration, RegiAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Exit, ExitAdmin)
#admin.site.register(logbook, loogbookadmin)
#admin.site.register(UnregisteredVehicle,UnregisteredVehicleAdmin)
admin.site.register(History,historyadmin)
#admin.site.register(HistoryUnregistered,HistoryUnregisteredAdmin)

