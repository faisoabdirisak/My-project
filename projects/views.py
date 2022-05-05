from urllib.parse import _NetlocResultMixinStr
from django.shortcuts import render
from .models import Project
projectsList =[
    {
        'id':'1',
        'title':'GithubSearch',
        'description':'uses to search github profile'
    },
     {
        'id':'2',
        'title':'GithubSearch2',
        'description':'uses to search github profile'
    }, 
    {
        'id':'3',
        'title':'GithubSearch3',
        'description':'uses to search github profile'
    },
     {
        'id':'4',
        'title':'GithubSearch4',
        'description':'uses to search github profile'
    }
]

def projects(request):
    projects=Project.objects.all
    context={'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj=Project.objects.get(id=pk)
    tags=projectObj.tags.all()
    context={'project':projectObj, 'tags':tags}
    return render(request, 'projects/single-project.html', context)   
