from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppAdopcion.models import Animal, Adoptante, Solicitud
from .forms import AnimalForm, AdoptanteForm, SolicitudForm
from django.views.generic import TemplateView
from django.views.generic import ListView
from AppAdopcion.models import Animal
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class TiendaView(ListView):
    model = Animal
    template_name = "AppAdopcion/index.html"
    context_object_name = "animales"
    paginate_by = 4  # opcional, 9 productos por página

class BuscarAnimalView(ListView):
    model = Animal
    template_name = "AppAdopcion/buscar.html"
    context_object_name = "resultados"

    def get_queryset(self):
        q = self.request.GET.get("q", "").strip()
        if q:
            return Animal.objects.filter(
                Q(nombre__icontains=q) | Q(especie__icontains=q)
            )
        return Animal.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "").strip()
        return context



class InicioView(TemplateView):
    template_name = "AppAdopcion/inicio.html"
# -------------------
# ANIMAL
# -------------------
class AnimalListView(ListView):
    model = Animal
    template_name = "AppAdopcion/animales.html"
    context_object_name = "animales" 
    paginate_by = 6   

class AnimalDetailView(DetailView):
    model = Animal
    template_name = "AppAdopcion/animal_detail.html"
    context_object_name = "animal"

class AnimalDeleteView(DeleteView): 
    model = Animal 
    template_name = "AppAdopcion/animal_delete.html" 
    success_url = reverse_lazy('animales_list')    


class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = "AppAdopcion/animal_create.html"
    success_url = reverse_lazy("animales_list")


class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = "AppAdopcion/animal_update.html"
    success_url = reverse_lazy("animales_list")


# -------------------
# ADOPTANTE
# -------------------

class AdoptanteListView(LoginRequiredMixin, ListView):
    model = Adoptante
    template_name = "AppAdopcion/adoptantes.html"
    context_object_name = "adoptantes"


class AdoptanteDetailView(DetailView):
    model = Adoptante
    template_name = "AppAdopcion/adoptante_detail.html"
    context_object_name = "adoptante"


class AdoptanteCreateView(CreateView):
    model = Adoptante
    form_class = AdoptanteForm
    template_name = "AppAdopcion/adoptante_create.html"
    success_url = reverse_lazy("adoptantes_list")


class AdoptanteUpdateView(UpdateView):
    model = Adoptante
    form_class = AdoptanteForm
    template_name = "AppAdopcion/adoptante_update.html"
    success_url = reverse_lazy("adoptantes_list")


# -------------------
# SOLICITUD
# -------------------
class SolicitudListView(ListView):
    model = Solicitud
    template_name = "AppAdopcion/solicitudes.html"
    context_object_name = "solicitudes"


class SolicitudDetailView(DetailView):
    model = Solicitud
    template_name = "AppAdopcion/solicitud_detail.html"
    context_object_name = "solicitud"


class SolicitudCreateView(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = "AppAdopcion/solicitud_create.html"
    success_url = reverse_lazy("solicitudes_list")


class SolicitudUpdateView(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = "AppAdopcion/solicitud_update.html"
    success_url = reverse_lazy("solicitudes_list")
