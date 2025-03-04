from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Profile, Link


# Create your views here.
class LinkListview(ListView):
    # by default it'll look for link_list.html template (<model_name>_list.html)
    # By default, the context is accesseble via `object_list` in the template.
    model = Link


class LinkCreateView(CreateView):
    model = Link
    # This will also create the *form* for us (no need to add it in forms.py)
    # But we still need to specify what fields is required to show.
    # It'll be looking for the template **link_form.html***
    # the form will be accessible via variable `form` in the template.
    fields = "__all__"
    # Where to send the user upon successfully creation of the link.
    success_url = reverse_lazy('link-list')


class LinkUpdateView(UpdateView):
    # N.B. `UpdateView` shares the same template as `CreateView`
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')
    # This looks for the template <model_name>_confirm_delete.html (here: link_confirm_delete.html)
    # also provides form to submit to delete the item


def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    # since in `Link` model, we've profided the `profile` field like so:
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')
    # we can access the links related to a profile like the following.
    # i.e., becaue of: related_name='links'
    links = profile.links.all()

    ctx = {
        'profile': profile,
        'links': links
    }

    return render(request, 'link_plant/profile.html', context=ctx)
