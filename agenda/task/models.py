from django.db import models
from django.conf import settings


class Task(models.Model):
	PRIMARIO = 1
	SECUNDARIO = 2

	GROUP_CHOICES = (
		(PRIMARIO, 'PRIMARIO'),
		(SECUNDARIO, 'SECUNDARIO'),
	)

	title = models.CharField( max_length=50, verbose_name='Título')
	description = models.TextField(max_length=150, verbose_name='Descrição')
	date_created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	date_updated = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)
	group = models.IntegerField(choices=GROUP_CHOICES, default=1)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'
