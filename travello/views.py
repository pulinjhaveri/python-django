from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request): 
    
    if request.method == 'POST':
        print('method is now',request.method)
        data = request.POST.copy()
        print(data.get('name'))
        
        newdest = Destination()
        newdest.name = data.get('name')
        newdest.desc = data.get('desc')
        newdest.img = data.get('name')
        newdest.price = int(data.get('price'))
        newdest.save()
        # print(request.POST['desc'])
        
    lst = {
        'list': Destination.objects.all()
    }
    #print(lst)
    return render(request,'index.html',lst)