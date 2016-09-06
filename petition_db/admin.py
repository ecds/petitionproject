# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export.admin import ExportActionModelAdmin
from petition_db.models import Authors, Texts, Prefectures


class TextsInline(admin.StackedInline):
    model = Texts.authors_set.related.through

class AuthorsResource(resources.ModelResource):
    class Meta:
        model = Authors
        fields = ('id', 'Author', 'Author_prefecture', 'Birth_year', 'Death_year', 'Details', 'Office', 'Other_names', 'Rank', 'Romanized_name', 'Sources', 'Status', 'urls')
        
class AuthorsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Author','Office','Romanized_name', 'Sources', 'Status')
    resource_class = AuthorsResource
    search_fields = ('Author','Office','Romanized_name', 'Sources', 'Status')
    ordering = ('Author',)
    filter_horizontal = ('Petitions',)
    inlines = [TextsInline,]

class AuthorInline(admin.StackedInline):
    model = Authors.Petitions.through

class TextsResource(resources.ModelResource):
    Prefecture = fields.Field(
        column_name='Prefecture',
        attribute='Prefecture',
        widget=ForeignKeyWidget(Prefectures, 'Prefectures'))
    class Meta:
        model = Texts
        fields = ('id', 'Sort_key', 'Title', 'Clean_text', 'Year', 'Month', 'Day', 'Number_in_arabic_numbers', 'Original_or_copy', 'Date_in_Japanese', 'Paper_type', 'Prefecture', 'Detailed_location', 'Temp_residence', 'Author_position', 'Author', 'Addressee', 'Archive', 'Date_unclear', 'Title_source', 'Ravina_checked', 'Armstrong_checked', 'Corrections', 'Full_text_with_CR')

class TextsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Sort_key','Title','Year')
    resource_class = TextsResource
    search_fields = ('Sort_key','Title','Year')
    ordering = ('Sort_key',)
#    filter_horizontal = ('Authors',)
    readonly_fields = ("Last_action",)
    inlines = [AuthorInline,]

class PrefecturesResource(resources.ModelResource):
    class Meta:
        model = Prefectures
        fields = ('id', 'Prefectures',)

class PrefecturesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PrefecturesResource


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Texts, TextsAdmin)
admin.site.register(Prefectures, PrefecturesAdmin)
