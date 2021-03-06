from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.models import Character

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def character_index(request):
    chars = Character.objects.all()
    return render(request, 'characters/index.html', { 'chars': chars })

def char_detail(request, char_id):
    char = Character.objects.get(id=char_id)
    return render(request, 'characters/detail.html', { 'char': char })

class CharCreate(CreateView):
    model = Character
    fields = ['name', 'year', 'ability_score', 'description']
    success_url = '/characters/'

class CharUpdate(UpdateView):
    model = Character
    fields = ['year', 'ability_score', 'description']

class CharDelete(DeleteView):
    model = Character
    success_url = '/characters/'