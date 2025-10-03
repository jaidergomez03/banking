
from django.contrib import admin
from .models import Country,Department,City,User # Importando tus modelos
# Register your models here.
#admin.site.register(Countries)
#admin.site.register(Departments)
#admin.site.register(Cities)
#admin.site.register(Users)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    display_data= ('name', 'abrev', 'get_status')
    list_filter= ()  # or other fields that exist, e.g. ('name',)
    search_fields= ('name', 'abrev')
    ordering= ('id',)

    def get_status(self, obj):
        return 'Active' if obj.status==True else 'Inactive'
    get_status.short_description = 'Status'
