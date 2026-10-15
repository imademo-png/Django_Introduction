from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from ..models import Festival

# def index(request):
#     return HttpResponse(Festival.__str__)

def index(request):
    return HttpResponse("Hello, world. You're at the Festival index.")


class FestivalListView(ListView):
    model = Festival
    template_name = 'festivals/list.html'
    context_object_name = 'festivals'


class FestivalDetailView(DetailView):
    model = Festival
    template_name = 'festivals/detail.html'
    context_object_name = 'festival'
    pk_url_kwarg = 'fest_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.object.events.all()
        return context
