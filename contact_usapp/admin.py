from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at','is_resolved','message')
    list_filter = ('is_resolved','created_at')
    list_editable = ('is_resolved',)

admin.site.register(Contact,ContactAdmin)
