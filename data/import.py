import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GameGen.settings")
app_root = os.path.dirname(os.path.dirname(__file__))
if app_root not in sys.path:
    sys.path.append(app_root)

import django
django.setup()
from Charades import models as c_models

def import_charade_words(category_name, file_name):
    print('importing category "%s"...'%(category_name,), end='')
    category = c_models.Category()
    category.name = category_name
    category.save()
    print('done')

    f = open(os.path.dirname(__file__) + '/' + file_name)
    words = f.read().split('\n')
    for w in words:
        print('    importing word "%s"...'%(w,), end='')
        word = c_models.Word()
        word.category = category
        word.word = w
        word.save()
        print('done')

import_charade_words('Easy', 'charades/easy.txt')
import_charade_words('Medium', 'charades/medium.txt')
import_charade_words('Hard', 'charades/hard.txt')
import_charade_words('Very Hard', 'charades/very-hard.txt')
