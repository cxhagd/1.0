# diary/models.py
from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='diary_images/', blank=True, null=True)

    def __str__(self):
        return self.title


from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['date', 'content', 'image']

from django.shortcuts import render, redirect
from .forms import DiaryEntryForm

def diary_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, request.FILES)
        if form.is_valid():
            diary_entry = form.save(commit=False)
            diary_entry.user = request.user
            diary_entry.save()
            return redirect('some_view')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/diary_form.html', {'form': form})

