from django.contrib import admin
from .models import Operator, Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'deadline')
    list_filter = ('title', 'created_by', 'deadline', 'is_urgent')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Todo, TodoAdmin)
admin.site.register(Operator)
