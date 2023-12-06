from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import Cours
from .forms import CourForm, NoteForm

# Create your views here.
def index(req):
    cours = Cours.objects.all()
    return render(req, 'index.html', {'cours': cours})
    # return HttpResponse("Hello, world. You're at the polls index.")

def courView(req, cour_id):
    cour = get_object_or_404(Cours, pk=cour_id)
    return render(req, 'details.html', {'cour': cour})


def courCreate(req):
    if req.method == 'POST':
        form = CourForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app')
    else:
        form = CourForm()
    
    return render(req, 'form.html', {'form': form})

def courEdit(req, cour_id):
    cour = get_object_or_404(Cours, pk=cour_id)
    if req.method == 'POST':
        form = CourForm(req.POST, instance=cour)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app')
    else:
        form = CourForm(instance=cour)
    
    return render(req, 'form.html', {'form': form})


def courNote(req, cour_id):
    cour = get_object_or_404(Cours, pk=cour_id)
    if req.method == 'POST':
        form = NoteForm(req.POST, instance=cour)
        if form.is_valid():
            note = form.cleaned_data['note']
            actualNote = cour.note
            noteNumber = cour.numberOfNote

            moy = (actualNote * noteNumber + note) / (noteNumber + 1)
            cour.note = moy
            cour.numberOfNote = cour.numberOfNote + 1
            cour.save()
            return HttpResponseRedirect('/app')
    else:
        form = NoteForm()
    
    return render(req, 'form.html', {'form': form})
