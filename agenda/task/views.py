from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializer import TaskSerializer
from .models import Task


class TaskListView(APIView):
	serializer_class = TaskSerializer

	def get(self, request, format=None):
		serializer = self.serializer_class(Task.objects.all(), many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response({'message': 'Erro ao criar Task'}, status=status.HTTP_409_CONFLICT)


class TaskView(APIView):
	serializer_class = TaskSerializer
	
	def get(self, request, pk, format=None):
		try:
			serializer = self.serializer_class(Task.objects.get(pk=pk))
			return Response(serializer.data)
		except Exception as e:
			Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, pk, format=None):
		try:
			serializer = Task.objects.get(pk=pk)
			serializer.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		except Exception as e:
			Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, pk, format=None):

		serializer = self.serializer_class(Task.objects.get(pk=pk), data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def tasks_exibir(request):
	tasks = Task.objects.all()
	context = {'task' : tasks}
	return render(request, 'task/exibir_tasks.html', context)

