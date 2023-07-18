from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Comment, Project
from .serializers import TaskSerializer, CommentSerializer, ProjectSerializer


# Create your views here.

class TaskAPIView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ProjectAPIView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
