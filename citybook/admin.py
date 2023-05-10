from django.contrib import admin
from django.contrib.auth.models import Group
from citybook.models import Category, City, Contact, Place

admin.site.unregister(Group)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass