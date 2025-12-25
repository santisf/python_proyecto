from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppAdopcion.models import Animal, Adoptante, Solicitud
from .forms import AnimalForm, AdoptanteForm, SolicitudForm
from django.views.generic import TemplateView
from django.views.generic import ListView
from AppAdopcion.models import Animal
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# AppAdopcion/views.py (o views_clases.py)
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Solicitud, Animal
from .forms import SolicitudForm



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


"""class SolicitudCreateView(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = "AppAdopcion/solicitud_create.html"
    success_url = reverse_lazy("solicitudes_list")"""




@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class SolicitudCreateView(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'AppAdopcion/solicitud_create.html'
    success_url = reverse_lazy('solicitudes_list')

    def dispatch(self, request, *args, **kwargs):
        animal_pk = self.kwargs.get('animal_pk')
        self.animal = get_object_or_404(Animal, pk=animal_pk) if animal_pk else None
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        return initial

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['animal'] = getattr(self, 'animal', None)
        return ctx

    def form_valid(self, form):
        # asignar user y animal
        form.instance.user = self.request.user
        if getattr(self, 'animal', None):
            form.instance.animal = self.animal

        # actualizar nombre/apellido del User si cambiaron
        first = form.cleaned_data.get('first_name')
        last = form.cleaned_data.get('last_name')
        user = self.request.user
        changed = False
        if first is not None and first != user.first_name:
            user.first_name = first
            changed = True
        if last is not None and last != user.last_name:
            user.last_name = last
            changed = True
        if changed:
            user.save()

        return super().form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class SolicitudUpdateView(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'AppAdopcion/solicitud_update.html'
    success_url = reverse_lazy('solicitudes_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.object.user.first_name
        initial['last_name'] = self.object.user.last_name
        return initial

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['animal'] = self.object.animal
        return ctx

    def form_valid(self, form):
        # actualizar nombre/apellido del user si cambian
        first = form.cleaned_data.get('first_name')
        last = form.cleaned_data.get('last_name')
        user = self.object.user
        changed = False
        if first is not None and first != user.first_name:
            user.first_name = first
            changed = True
        if last is not None and last != user.last_name:
            user.last_name = last
            changed = True
        if changed:
            user.save()
        return super().form_valid(form)




class SolicitudListView(LoginRequiredMixin, ListView):
    model = Solicitud
    template_name = 'AppAdopcion/solicitudes.html'
    context_object_name = 'solicitudes'
    paginate_by = 20

    def get_queryset(self):
        # Si querés que el staff vea todas las solicitudes:
        if self.request.user.is_staff:
            return Solicitud.objects.all().select_related('animal','user').order_by('-fecha_de_solicitud')
        # Usuario normal: solo sus solicitudes
        return Solicitud.objects.filter(user=self.request.user).select_related('animal','user').order_by('-fecha_de_solicitud')


class SolicitudDeleteView(LoginRequiredMixin, DeleteView):
    model = Solicitud
    template_name = 'AppAdopcion/solicitud_confirm_delete.html'  # opcional
    success_url = reverse_lazy('solicitudes_list')

    def get_queryset(self):
        qs = super().get_queryset().select_related('user')
        # solo el owner o staff puede borrar
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)
