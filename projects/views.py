from django.shortcuts import render
from .models import Project
# Create your views here.

def index(request):
    projects = Project.objects
    return render(request, 'projects/index.html', {'projects':projects})
    