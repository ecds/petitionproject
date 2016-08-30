from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export.admin import ExportActionModelAdmin
from petition_db.models import Authors, Texts



class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('Author','Office','Romanized_name')
    search_fields = ('Author','Office','Romanized_name')
    ordering = ('Author',)
    filter_horizontal = ('Petitions',)

class TextsAdmin(admin.ModelAdmin):
    list_display = ('Sort_key','Title','Year')
    search_fields = ('Sort_key','Title','Year')
    ordering = ('Sort_key',)
    filter_horizontal = ('Authors',)
    readonly_fields = ("Last_action",)

admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Texts, TextsAdmin)
