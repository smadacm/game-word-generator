from django.shortcuts import render
from django import views
from django.views.generic import TemplateView, RedirectView
from Charades import models

# Create your views here.
class Word(TemplateView):
    template_name = 'charades/word.html'

    def get_context_data(self, **kwargs):
        context = super(Word, self).get_context_data(**kwargs)

        categories = models.Category.objects.all()
        all_category_ids = [str(x.id) for x in categories]
        if context['category_id'] not in all_category_ids:
            context['category_id'] = 1
        current_category = models.Category.objects.get(id=context['category_id'])
        word = models.Word.random(context['category_id'])

        context['word'] = word
        context['categories'] = categories
        context['current_category'] = current_category

        return context

class Index(RedirectView):
    permanent = True
    pattern_name = "charades.word"
