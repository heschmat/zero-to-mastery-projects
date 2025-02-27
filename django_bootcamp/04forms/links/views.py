from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm

# Create your views here.
def index(request):
    links = Link.objects.all()
    ctx = {'links': links}
    return render(request, 'links/index.html', context=ctx)

# outsite.net/google => www.google.com
def forward_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.update_click()  # increment the click view

    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        # request.POST =>
        # <QueryDict: {'csrfmiddlewaretoken': [''], 'name': ['a'], 'url': ['https://www.example.com/'], 'slug': ['c']}>
        form = LinkForm(request.POST)
        if form.is_valid():
            # Save the cleaned data & return user to homepage.
            # form.cleaned_data => {'name': 'a', 'url': 'https://www.example.com/', 'slug': 'c'}
            form.save()
            return redirect(reverse('homepage'))
    else:
        form = LinkForm()
    ctx = {'form': form}
    return render(request, 'links/add_link.html', ctx)
