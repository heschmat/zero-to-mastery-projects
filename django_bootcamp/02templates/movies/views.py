from django.shortcuts import render

# Create your views here.
def home(request):
    movies = [
        'Creed I',
        'The Imitation Game',
        'On the Basis of Sex',
        'The Intouchables',
    ]

    return render(request, 'movies/index.html', context={'movies': movies})

def about(request):
    return render(request, 'movies/about.html', context={})
