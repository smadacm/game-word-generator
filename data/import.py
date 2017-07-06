import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GameGen.settings")
app_root = os.path.dirname(os.path.dirname(__file__))
if app_root not in sys.path:
    sys.path.append(app_root)

import django
django.setup()
from Charades import models as c_models

category = c_models.Category()
category.name = 'Easy'
category.save()
f = open(os.path.dirname(__file__) + '/charades/easy.txt')
words = f.read().split('\n')
for w in words:
    print('importing %s...'%(w,), end='')
    word = c_models.Word()
    word.category = category
    word.word = w
    word.save()
    print('done')