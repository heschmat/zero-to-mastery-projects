from django.urls import path

from .views import LinkListview, LinkCreateView, LinkUpdateView, LinkDeleteView

urlpatterns = [
    # 2nd argument should be a `view with a _ResponseType`
    # hence, wenn it's a class, we add `.as_view()`
    path('', LinkListview.as_view(), name='link-list'),
    path('link/create/', LinkCreateView.as_view(), name='link-create'),
    path('link/<int:pk>/update', LinkUpdateView.as_view(), name='link-update'),
    path('link/<int:pk>/delete/', LinkDeleteView.as_view(), name='link-delete')
]
