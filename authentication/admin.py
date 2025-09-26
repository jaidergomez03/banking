
from django.contrib import admin
from .models import Countries,Departments,Cities,Users # Importando tus modelos
# Register your models here.
admin.site.register(Countries)
admin.site.register(Departments)
admin.site.register(Cities)
admin.site.register(Users)