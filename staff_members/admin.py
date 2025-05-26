from django.contrib import admin
from .models import Staff_member


class Staff_memberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
    prepopulated_fields = {"slug": ("firstname", "lastname")}
admin.site.register(Staff_member, Staff_memberAdmin)

# Register your models here.
