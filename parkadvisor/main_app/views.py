from django.shortcuts import render, redirect


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
from django.http import HttpResponse

def home(request):
    return redirect(request, '/parks')

def about(request):
    return render(request, 'about.html')

def parks_index(request):
    return render(request, 'parks/index.html', { 'cats': cats })