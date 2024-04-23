from django.contrib import admin

# Register your models here.

from .models import Departments
admin.site.register(Departments)

from .models import Employees
admin.site.register(Employees)
