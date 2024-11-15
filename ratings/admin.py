from django.contrib import admin
from .models import Human, RatingCount, Category



class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'added_by']  # Ensure 'added_by' is part of the model fields

admin.site.register(Human, HumanAdmin)
admin.site.register(RatingCount)
admin.site.register(Category)
