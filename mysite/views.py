from django.shortcuts import render,get_object_or_404
from .forms import NewNoteForm
from .models import notes
from django.utils import timezone
# Create your views here.

def home(request):
    all_notes = notes.objects.order_by('published_date')
    return render(request,'home.html',{'notes':all_notes})

def login(request):
    return render(request,'login.html',{})

def sign_up(request):
    return render(request,'thanks-for-new-registration.html',{})

def note_detail(request,id = None):
    current_note = get_object_or_404(notes,id=id)
    return render(request,'single-note.html',{'this_note':current_note})

def scrum(request):
    return render(request,'scrum.html',{})

def create_notes(request):
    form = NewNoteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return  render(request, 'home.html', {})

    return render(request,'create-note.html',{'form': form})
