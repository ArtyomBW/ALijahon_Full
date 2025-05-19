from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Product, AdminSetting, User, Payment


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(ModelAdmin):

    exclude = 'slug',

@admin.register(AdminSetting)
class AdminSettingAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = 'card_number' , 'pay_amount' , 'pay_status' , 'receipt'




