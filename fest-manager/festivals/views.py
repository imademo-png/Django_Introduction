from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Festival

# def index(request):
#     return HttpResponse(Festival.__str__)

def index(request):
    return HttpResponse("Hello, world. You're at the Festival index.")


def festival_list(request):
    festivals = Festival.objects.all() 
    context={
    'festivals':festivals
    }
    return render(request, 'festivals/list.html', context)


def festival_detail(request, fest_id):
    festival = get_object_or_404(Festival, pk=fest_id)
    events = festival.events.all()
    events_data = []
    for ed in events:
        events_data.append({
            'name': ed.name,
            'status':ed.status()
            })
    return render(request, 'festivals/detail.html', {'festival': festival,'events': events_data})