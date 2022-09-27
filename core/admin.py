from django.contrib import admin
from .models import SystemConfig, Department, ProgramGroup, Staff, Program, Building, Room

class SystemConfigAdmin(admin.ModelAdmin):
	list_display = ('key', 'value')
	ordering = ('key',)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'color', 'image')
	prepopulated_fields = {'slug': ('name',)}
	ordering = ('name',)

class ProgramGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'color', 'image')
	prepopulated_fields = {'slug': ('name',)}
	ordering = ('name',)

class StaffAdmin(admin.ModelAdmin):
	list_display = ('name', 'role', 'building', 'room')
	ordering = ('name',)
	list_filter = ('role', 'room__building')
	search_fields = ('name', 'role')

class ProgramAdmin(admin.ModelAdmin):
	list_display = ('name', 'department', 'group')
	ordering = ('name', 'department', 'group')
	list_filter = ('department', 'group')

class BuildingAdmin(admin.ModelAdmin):
	list_display = ('name',)

class RoomAdmin(admin.ModelAdmin):
	list_display = ('name', 'building')
	list_filter = ('building',)


# Register your models here.
admin.site.register(SystemConfig, SystemConfigAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ProgramGroup, ProgramGroupAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)