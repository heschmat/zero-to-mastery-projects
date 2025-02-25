
from django.urls import path

from .views import index, job_detail

urlpatterns = [
    path('', index, name='homepage'),
    path('jobs/<int:pk>', job_detail, name='job-detail'),
]
