from django.contrib import admin
from .models import Employe


class EmployeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employe, EmployeAdmin)
