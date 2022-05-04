from urllib.parse import _NetlocResultMixinStr
from django.shortcuts import render

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
    context={'projects':projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj=None
    for i in projectsList:
        if i['id']==pk:
            projectObj=i
    context={'project':projectObj}
    return render(request, 'projects/single-project.html', context)   
