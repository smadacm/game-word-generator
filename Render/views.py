import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class Index(TemplateView):
    template_name = 'render/home.html'

def wordsForApp(request):
    data = {
        'categories': {
            1: 'Easy',
            2: 'Medium',
            3: 'Hard',
        },
        'words': {
             1: 'cat',
             2: 'dog',
             3: 'floor',
             4: 'sun',
             5: 'tree',
             6: 'bobby pin',
             7: 'family',
             8: 'broken heart',
             9: 'couch',
            10: 'bbq',
            11: 'highway',
            12: 'picture',
        },
        'game_category_word': (
            # (game_id, category_id, word)
            (1, 1, 1),
            (1, 1, 2),
            (1, 1, 3),
            (1, 2, 4),
            (1, 2, 5),
            (1, 3, 6),
            (1, 3, 7),
            (2, 1, 1),
            (2, 1, 2),
            (2, 1, 9),
            (2, 2, 7),
            (2, 2, 11),
            (2, 3, 8),
            (2, 3, 10),
        ),
    }

    return HttpResponse(json.dumps(data))
