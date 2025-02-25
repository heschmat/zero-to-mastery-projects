from django.shortcuts import render, get_object_or_404

from .models import JobPosting

# Create your views here.
def index(request):
    # active_jobs = JobPosting.objects.all()
    active_jobs = JobPosting.objects.filter(is_active=True)
    ctx = {'jobs': active_jobs}
    return render(request, 'job_board/index.html', context=ctx)

def job_detail(request, pk):
    # job = JobPosting.objects.get(pk=pk)
    job = get_object_or_404(JobPosting, pk=pk)
    return render(request, 'job_board/detail.html', context={'job': job})
