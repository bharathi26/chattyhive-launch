__author__ = 'xurxo'
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import InterestedUser

class InterestedUserResource(resources.ModelResource):

    class Meta:
        model = InterestedUser


class InterestedUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = InterestedUserResource
    list_display = ('email', 'name', 'subject', 'content', 'via')
    pass

admin.site.register(InterestedUser, InterestedUserAdmin)