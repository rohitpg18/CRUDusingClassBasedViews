from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from crud.models import Student


class StudentAdmin(ImportExportModelAdmin , admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'email']


admin.site.register(Student , StudentAdmin)