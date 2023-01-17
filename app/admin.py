from django.contrib import admin

import app.models as am
# Register your models here.

@admin.register(am.Element)
class ElementAdmin(admin.ModelAdmin):
    pass
