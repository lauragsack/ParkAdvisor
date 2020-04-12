from django.shortcuts import render, redirect
from .models import Park, Review, User
from .forms import ReviewForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#API RELATED
import requests
from rest_framework import status 
from rest_framework.response import Response 
from django.http import HttpResponse



# Create your views here.
def home(request):
    return redirect(request, 'parks/')

def about(request):
    return render(request, 'about.html')

def parks_index(request):
    parks = Park.objects.all()
    return render(request, 'parks/index.html', { 'parks': parks })

def parks_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    review_form = ReviewForm()
    this_parks_reviews = park.review_set.all()
    return render (request, 'parks/detail.html', {
        'park': park,
        'review_form': review_form,
        'reviews': this_parks_reviews
    })

@login_required
def add_review(request, park_id):

    

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.park_id = park_id
            new_review.user = request.user
            new_review.save()   
            return redirect('detail', park_id)
    else:
        form = ReviewForm()
    context = { 'form': form }
    return render(request, 'reviews/review_form.html', { 'form': form })


@login_required
def reviews_update(request, review_id):
    review = Review.objects.get(id=review_id)
    park_id = review.park.id
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect ('detail', park_id)
    else: 
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', { 'form': form })

@login_required
def reviews_delete(request, review_id):
    review = Review.objects.get(id=review_id)
    park_id = review.park.id
    Review.objects.get(id=review_id).delete()
    return redirect('detail', park_id)


@login_required
def reviews_index(request):
    reviews = Review.objects.filter(user=request.user)
    return render(request, 'reviews/review_list.html', { 'reviews': reviews })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def external_api(request):
    url = 'https://developer.nps.gov/api/v1/parks?limit=1&api_key=65cD2Pey6zgKAXKmKA71wA6sHmuIcsAdiSs5xmhp'
    # headers = {'api_key': '65cD2Pey6zgKAXKmKA71wA6sHmuIcsAdiSs5xmhp'}
    response = requests.get(url)
    data = response.json()
    print(data["data"][0]["states"])

    new_park = Park.objects.create(name="Ajay", location="Home", entrance_fee=3, description="blah", phone="243433444", website="www.google.com", open=True, image="www.yahoo.com", avg_rating=3.6)

    # print(data[0]["states"])
    # data = response.json()
    # print(data)
    # parks_data = response.json()
    # print(parks_data)
    return render(request, 'parks/test.html', {'data': data})


