from django.urls import path

from .views import index, forward_link, add_link

urlpatterns = [
    path('', index, name='homepage'),
    path('<str:link_slug>', forward_link, name='forward-link'),
    path('link/add', add_link, name='add-link')
]
