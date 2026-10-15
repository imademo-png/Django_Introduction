# Vues "site web" : elles renvoient des pages HTML via des templates.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

# ".." = remonter d'un dossier (on est dans festivals/views/, models.py est dans festivals/)
from ..models import Festival

# def index(request):
#     return HttpResponse(Festival.__str__)

def index(request):
    return HttpResponse("Hello, world. You're at the Festival index.")


class FestivalListView(ListView):
    # Modèle à lister -> queryset = Festival.objects.all()
    model = Festival
    # Template utilisé (sinon Django chercherait festivals/festival_list.html)
    template_name = 'festivals/list.html'
    # Nom de la variable dans le template (sinon ce serait "object_list" / "festival_list")
    context_object_name = 'festivals'


class FestivalDetailView(DetailView):
    model = Festival
    template_name = 'festivals/detail.html'
    # Nom de la variable dans le template : {{ festival.name }}
    context_object_name = 'festival'
    # Par défaut DetailView attend <int:pk> dans l'URL ; notre URL utilise <int:fest_id>
    pk_url_kwarg = 'fest_id'

    # Ajoute des données supplémentaires au contexte du template
    def get_context_data(self, **kwargs):
        # On récupère le contexte de base (qui contient déjà "festival")
        context = super().get_context_data(**kwargs)
        # self.object = le festival trouvé ; "events" vient du related_name du ForeignKey
        context['events'] = self.object.events.all()
        return context
