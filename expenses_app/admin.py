from django.contrib import admin

from .models import Category, Shop, BillRow, Bill

admin.site.register(Category)
admin.site.register(Shop)


class BillRowInline(admin.TabularInline):
    model = BillRow
    extra = 3


class BillAdmin(admin.ModelAdmin):
    inlines = [BillRowInline]

admin.site.register(Bill, BillAdmin)
