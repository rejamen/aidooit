"""Register modules to admin."""
from django.contrib import admin
from .models import Person, PersonHistory
# Register your models here.


class HistoryInline(admin.TabularInline):
	"""Set inline records."""

	model = PersonHistory
	extra = 1


class PersonAdmin(admin.ModelAdmin):
	"""Modify what to admin in Person model."""

#	fields = ['name', 'last_name'] #use this only for change the order
	fieldsets = [
		(None, {'fields': ['name', 'last_name']}),
		('Other data', {'fields': ['mobile', 'phone', 'email']})
	]
	inlines = [HistoryInline]

admin.site.register(Person, PersonAdmin)
