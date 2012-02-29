from django.db import models

class Film(models.Model):
	name = models.CharField(max_length=24,unique=True)
	longname = models.CharField(max_length=24)
	director = models.CharField(max_length=24)
	note = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name
				
class Sequence(models.Model):
	film = models.ForeignKey(Film)
	name = models.CharField(max_length=12)
	def __unicode__(self):
		return self.name

class Shot(models.Model):
	sequence = models.ForeignKey(Sequence)
	name = models.CharField(max_length=12)
	pim = models.IntegerField()
	def __unicode__(self):
		return self.name
	def diff_acent(self):
		return 100 - self.pim
	diff_acent.short_description = 'differ a 100'
	def returnfilm(self):
		return self.sequence.film.name
	returnfilm.short_description = 'film parent'