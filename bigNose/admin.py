from django.contrib import admin
from bigNose.models import User, WordsCategories, Word

# Register your models here.
admin.register(User)
admin.register(Word)
admin.register(WordsCategories)
