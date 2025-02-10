from django.shortcuts import render
from .models import Dictionary  # impot the model Dictionary

# Create your views here.

def home(request):
    all_words = Dictionary.objects.all()
    # SORTING THE WORDS IN ALPHABETICAL ORDER 
    all_words = all_words.order_by('word')
    return render(request, 'dictapp/home.html',{
        'all_words': all_words
    })

def meaning(request, word):
    meaning = Dictionary.objects.get(word=word)
    meaning = meaning.meaning
    example = Dictionary.objects.get(word=word)
    example = example.example
  
    return render(request, 'dictapp/meaning.html', {
        'word': word,
        'meaning': meaning, 
        'example': example
    })
  
    