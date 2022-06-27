from django.shortcuts import render, redirect
from .models import WriteDown
from .forms import NoteForm

def home(request):

    context = {'notes':WriteDown.objects.all()}
    return render(request, 'base/home.html', context)

def detail(request, pk):

    notes = WriteDown.objects.get(id=pk)
    context = {'notes':notes}
    return render(request, 'base/detail.html', context)

def create_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/create_form.html', context)

def edit_note(request, pk):
    note = WriteDown.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/create_form.html', context)

def delete_note(request, pk):
    note = WriteDown.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    context = {'note':note}
    return render(request, 'base/delete_form.html', context)
