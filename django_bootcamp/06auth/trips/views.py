from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trips/index.html'


def trips_list(request):
    # Filter the trips to those of the user making the request only.
    trips = Trip.objects.filter(owner=request.user)
    ctx = {'trips': trips}
    return render(request, 'trips/trips_list.html', context=ctx)


class TripCreateView(CreateView):
    model = Trip
    fields = ['city', 'country']
    success_url = reverse_lazy('trip-list')

    def form_valid(self, form):
        # Automatically save the logged-in user as the owner of the created trip.
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    # This view looks for `<modelname>_detail.html` template
    # in our case: trip_detail.html
    model = Trip

    # We also want to show the related "Note"s
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        # As we set the `related_name` in the Note model for field `trip` to `notes`,
        # we can access a trip's related notes like: trip.notes
        context['notes'] = trip.notes.all()
        return context


class NoteDetailView(DetailView):
    model = Note


class NoteListView(ListView):
    model = Note

    def get_queryset(self):
        # Filter the notes based on the user sending the request.
        # `owner` is field of `trip` which is **foreign key** to note:
        # to access that, we use `__` => trip__owner
        return Note.objects.filter(trip__owner=self.request.user)


class NoteCreateView(CreateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note-list')

    def get_form(self):
        form = super().get_form()
        # In the form, limit the `trip` dropdown
        # to only the trips for the user sending the request.
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form


class NoteUpdateView(UpdateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note-list')

    def get_form(self):
        form = super().get_form()
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')


class TripUpdateView(UpdateView):
    model = Trip
    fields = ['city', 'country']  # don't show the `owner` as it's the user
    success_url = reverse_lazy('trip-list')
    # template it looks for: <modelname>_form


class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')
