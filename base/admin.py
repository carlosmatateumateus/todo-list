from django.contrib import admin
from .models import WriteDown

@admin.register(WriteDown)

class WriteDownAdmin(admin.ModelAdmin):
    ...