from django.shortcuts import render
from .models import Video
from django.contrib.auth.models import User
from django.http import HttpResponse

def indexes(request):
    if User:
   
        videos=Video.objects.all()
        context={'videos': videos}
        return render(request, 'videos/indexes.html', context)

def indexesOne(request):
    
       
        videos=Video.objects.all()
        context={'videos': videos}
        if User.is_nodeFullStack:
            return render(request, 'videos/indexes-1.html', context)
        else:
            return HttpResponse('wrong')
    
   