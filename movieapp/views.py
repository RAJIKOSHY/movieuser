from django.shortcuts import render,redirect
from .models import movie,User
from django.contrib.auth.decorators import login_required
from .forms import movieform




def index(request):
    Movie=movie.objects.all()
    context = {
         'movielist': Movie
    }
    return render(request,"index.html",context)
def details(request,movie_id):
    actor = movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie': actor})


@login_required()
def add_movie(request):
    if request.method == 'POST':
        form = movieform(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.creator = request.user
            movie.save()
            return redirect('/')
    else:
        form = movieform()
    return render(request, 'edit.html', {'form': form})

@login_required()
def update(request,id):
    Movie =movie.objects.get(id=id)

    if request.user == Movie.creator:
        form = movieform(request.POST or None, request.FILES, instance=Movie)
        if request.method=='POST':

            if form.is_valid():
                form.save()
                return redirect("/")
        return render(request, 'edit.html', {'movie': Movie, 'form': form})
    else:
        return render(request,'notallowed.html')


@login_required()
def delete(request,id):
    Movie = movie.objects.get(id=id)
    if request.user == Movie.creator:
        if request.method == 'POST':

            Movie.delete()
            return redirect("/")

        return render(request,"delete.html",{'movie':Movie})
    else:
        return render(request,'notallowed.html')

