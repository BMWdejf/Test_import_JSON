from django.contrib import admin

from main.models import Population


# Register your models here.

@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ('country', 'year', 'human_count')