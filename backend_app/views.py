from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

from .models import PostJob
from .serializers import *

# Create your views here.
# class PostJobView(viewsets.ModelViewSet):
#     serializer_class = PostJobSerializer
#     queryset = PostJob.objects.all()


@api_view(['GET', 'POST'])
def jobs_list(request):
    if request.method == 'GET':
        data = PostJob.objects.all()
        serializer = PostJobSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostJobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE']) 
def jobs_details(request, pk):
    try:
        post_job = PostJob.objects.get(pk=pk)
    except PostJob.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostJobSerializer(post_job, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post_job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)