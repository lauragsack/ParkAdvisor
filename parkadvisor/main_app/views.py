from django.shortcuts import render, redirect
from .models import Park, Review, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]

# Create your views here.
def home(request):
    return redirect(request, 'parks/')

def about(request):
    return render(request, 'about.html')

def parks_index(request):
    return render(request, 'parks/index.html', { 'cats': cats })

def parks_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    # review_form = ReviewForm()
    this_parks_reviews = park.review_set.all()
    return render (request, 'parks/detail.html', {
        'park': park,
        # 'review_form': review_form,
        'reviews': this_parks_reviews
    })