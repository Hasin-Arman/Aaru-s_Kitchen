from django.contrib import admin
from .models import recipyModel
# Register your models here.
class recipyModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["ingredients",]}
admin.site.register(recipyModel, recipyModelAdmin)