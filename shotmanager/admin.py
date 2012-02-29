from cgevam.shotmanager.models import *
from django.contrib import admin
from django.contrib.contenttypes import generic




class SequenceInline(admin.StackedInline):
	model= Sequence
	extra = 3

class ShotInline(generic.GenericTabularInline):
    model = Shot
	
class FilmAdmin(admin.ModelAdmin):
	fieldsets= [
			('Titre du Film',                   {'fields':['name']}),
			('Notes sur le film (ftp etc...)',  {'fields':['note']}),
			('Nom du real',                     {'fields':['director']}),
			('Nom court' ,                      {'fields':['longname']}),
	]
	inlines = [SequenceInline,ShotInline]
	list_display = ('longname','name', 'director', 'note')
	search_fields = ['name']


class SequenceAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ('name', 'film',)
	list_filter = ['film']

class ShotAdmin(admin.ModelAdmin):
	search_fields = ['sequence__film__name']
	list_display = ('name','sequence', 'pim', 'id', 'diff_acent', 'returnfilm' )
	list_editable =['pim']
	list_filter = ['name','sequence__film__name' ]
	actions =['resetpim']
	def resetpim(self, request, queryset):
		rows_updated=queryset.update(pim="12")
		if rows_updated == 1:
			message_bit = "1 shot pim was"
		else:
			message_bit = "%s shots pims were" % rows_updated
		self.message_user(request, "%s successfully reset." % message_bit)

admin.site.register(Film, FilmAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Shot, ShotAdmin)
