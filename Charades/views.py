from django.shortcuts import render
from django import views
from django.views.generic import TemplateView
from Charades import models

# Create your views here.
class Word(TemplateView):
    template_name = 'charades/word.html'

    def get_context_data(self, **kwargs):
        context = super(Word, self).get_context_data(**kwargs)
        word = models.Word.random(kwargs['category_id'])
        context['word'] = word
        return context
