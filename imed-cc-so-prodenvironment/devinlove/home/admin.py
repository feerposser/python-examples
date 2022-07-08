from django.contrib import admin

from .models import Declaration

class AdminDeclaration(admin.ModelAdmin):
    prepopulated_fields = {"url_slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.status = "E"
        
        return super().save_model(request, obj, form, change)

admin.site.register(Declaration, AdminDeclaration)
