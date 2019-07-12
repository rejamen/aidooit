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
	list_display = ('name', 'last_name', 'mobile', 'phone', 'email')
#	list_filter = ['name', 'mobile']
	search_fields = ['name', 'last_name', 'mobile','phone', 'email' ]


admin.site.register(Person, PersonAdmin)
