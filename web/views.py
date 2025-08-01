from django.shortcuts import render
from room.models import Room
from django.http import HttpResponseRedirect

def start_page(request) -> render:
    return render(
        request=request,
        template_name='pages/start.html',
        context={}
    )

def ide_page(request) -> render:
    parameters = request.GET 
    number = parameters.get('room')
    if number is None or not Room.objects.filter(number=number).exists():
        return HttpResponseRedirect('/start/')
    
    return render(
        request=request,
        template_name='pages/ide.html',
        context={
            'number': number
        }
    )