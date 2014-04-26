__author__ = 'xurxo'
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from models import InterestedUser

class InterestedUserResource(resources.ModelResource):

    class Meta:
        model = InterestedUser
        exclude = ('name', 'subject', 'content', 'via', )


class InterestedUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = InterestedUserResource
    pass

admin.site.register(InterestedUser, InterestedUserAdmin)