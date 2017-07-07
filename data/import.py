import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GameGen.settings")
app_root = os.path.dirname(os.path.dirname(__file__))
if app_root not in sys.path:
    sys.path.append(app_root)

import django
django.setup()
from Charades import models as c_models
from Pictionary import models as p_models

def import_words(category_name, file_name, cat_cls, word_cls):
    print('importing category "%s"...'%(category_name,), end='')
    category = cat_cls()
    category.name = category_name
    category.save()
    print('done')

    f = open(os.path.dirname(__file__) + '/' + file_name)
    words = f.read().split('\n')
    for w in words:
        if not w.strip(): continue
        print('    importing word "%s"...'%(w,), end='')
        word = word_cls()
        word.category = category
        word.word = w
        word.save()
        print('done')

def import_charade_words(category_name, file_name):
    import_words(category_name, file_name, c_models.Category, c_models.Word)

def import_pictionary_words(category_name, file_name):
    import_words(category_name, file_name, p_models.Category, p_models.Word)

import_charade_words('Easy', 'charades/easy.txt')
import_charade_words('Medium', 'charades/medium.txt')
import_charade_words('Hard', 'charades/hard.txt')
import_charade_words('Very Hard', 'charades/very-hard.txt')

import_pictionary_words('Easy', 'pictionary/easy.txt')
import_pictionary_words('Medium', 'pictionary/medium.txt')
import_pictionary_words('Hard', 'pictionary/hard.txt')
import_pictionary_words('Really Hard', 'pictionary/really-hard.txt')
import_pictionary_words('Idioms', 'pictionary/idioms.txt')
import_pictionary_words('Movies', 'pictionary/movies.txt')
import_pictionary_words('People & Characters', 'pictionary/people-characters.txt')
