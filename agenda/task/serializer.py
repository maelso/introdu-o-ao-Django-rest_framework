from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		depth = 1
		fields = ['id', 'title', 'description', 'date_created', 'date_updated', 'group']