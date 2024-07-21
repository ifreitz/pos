from django.contrib import admin

# Register your models here.
from ui.models import Category, Menu

admin.site.register(Category)
admin.site.register(Menu)
