from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import Entry
from app.forms import EntryForm
from app.decorators import user_is_entry_author
from django.contrib.auth.decorators import login_required




def index(request):
    entries = Entry.objects.all()
    return render(request, 'app/index.html', {'entries': entries})



def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry was successfully added!')
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'app/entry.html', { 'form': form })

@user_is_entry_author
def edit(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry was successfully edited!')
            return redirect('index')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'app/entry.html', { 'form': form })