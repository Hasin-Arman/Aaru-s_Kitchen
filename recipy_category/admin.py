from django.contrib import admin
from .models import category_model
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}

admin.site.register(category_model,categoryAdmin)