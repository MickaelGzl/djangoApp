from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import Cours
from .forms import CourForm

# Create your views here.
def index(req):
    cours = Cours.objects.all()
    return render(req, 'index.html', {'cours': cours})
    # return HttpResponse("Hello, world. You're at the polls index.")

def courView(req, cour_id):
    cour = get_object_or_404(Cours, pk=cour_id)
    return render(req, 'details.html', {'cour': cour})

def courCreate(req):
    return render(req, 'form.html', {'cour': None})

def courEdit(req, cour_id):
    if req.method == 'POST':
        form = CourForm(req.POST)
        if form.is_valid():
            form.save()
    else:
        cour = get_object_or_404(Cours, pk=cour_id)
        form = CourForm(instance=cour)
    
    return render(req, 'form.html', {'form': form})
