from django.contrib import admin
from customers.models import Customers, Users



class CustomersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fullname', 'current_balance')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'created_time', 'password', 'last_login', 'is_staff', 'is_superuser')

admin.site.register(Customers, CustomersAdmin)
admin.site.register(Users, UsersAdmin)

