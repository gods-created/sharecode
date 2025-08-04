from django.shortcuts import render
from room.models import Room
from django.http import HttpResponseRedirect
from enums import Languages

def start_page(request) -> render:
    return render(
        request=request,
        template_name='pages/start.html',
        context={
            'languages': [(index, item.value) for index, item in enumerate(Languages)]
        }
    )

def ide_page(request) -> render:
    parameters = request.GET 
    number = parameters.get('room')
    room = Room.objects.filter(number=number).first()
    if not room:
        return HttpResponseRedirect('/start/')
    
    return render(
        request=request,
        template_name='pages/ide.html',
        context={
            'number': number,
            'language': room.language
        }
    )