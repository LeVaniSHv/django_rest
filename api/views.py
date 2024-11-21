from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverView(request):
    
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}


    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    
    serializer = TaskSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['PUT'])
def taskUpdate(request, pk):
    
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task , data = request.data )
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    
    task = Task.objects.get(pk=pk)

    task.delete()

    return redirect('task-list')