from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trips/index.html'


def trips_list(request):
    # Filter the trips to those of the user making the request only.
    trips = Trip.objects.filter(owner=request.user)
    ctx = {'trips': trips}
    return render(request, 'trips/trips_list.html', context=ctx)
