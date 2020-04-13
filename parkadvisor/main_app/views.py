from django.shortcuts import render, redirect
from .models import Park, Review, User
from .forms import ReviewForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#API RELATED
import requests
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
    if len(this_parks_reviews) == 0:
        park.avg_rating = 0
    else:
        sum_reviews = 0
        for review in this_parks_reviews:
            sum_reviews += review.park_rating
            park.avg_rating = sum_reviews / len(this_parks_reviews)
    return render (request, 'parks/detail.html', {
        'park': park,
        'review_form': review_form,
        'reviews': this_parks_reviews,
        'park.avg_rating': park.avg_rating
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
def reviews_like(request, review_id):
    review = Review.objects.get(id=review_id)
    # likes = review.likes
    park_id = review.park.id
    if request.method == 'GET':
        review.likes += 1
        print('***************')
        print(review.likes)
        print('***************')
        review.save()
    return redirect('detail', park_id)

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

    #Working
    url = 'https://developer.nps.gov/api/v1/parks?limit=50&api_key=65cD2Pey6zgKAXKmKA71wA6sHmuIcsAdiSs5xmhp'
    response = requests.get(url)
    data = response.json()

    # print(data["data"][0]["states"])
    # print("---------------------------------------")
    # print(not(Park.objects.filter(name=park["fullName"]).exists()))
    # print("----------------------------------------")

    #Sort of working
    for park in data["data"]:
        #Filter out desigination and only create models for 'National Park'

        if( (not(Park.objects.filter(name=park["fullName"]).exists())) and (park["designation"] == "National Park") ):
            new_park = Park.objects.create(name=park["fullName"], location=park["addresses"][0],entrance_fee=int(float(park["entranceFees"][0]["cost"])), description=park["description"], phone=park["contacts"]["phoneNumbers"][0]["phoneNumber"], website=park["url"], open=True, image=park["images"][0]["url"], avg_rating=0)


    # new_park = Park.objects.create(name=data["data"][0]["fullName"], location=data["data"][0]["addresses"][0],
    #  entrance_fee=int(float(data["data"][0]["entranceFees"][0]["cost"])), description=data["data"][0]["description"], 
    #  phone=data["data"][0]["contacts"]["phoneNumbers"][0]["phoneNumber"], website="www.google.com", open=True, image="www.yahoo.com", avg_rating=3.6)

    # print(data[0]["states"])
    # data = response.json()
    # print(data)
    # parks_data = response.json()
    # print(parks_data)
    return render(request, 'parks/test.html', {'data': data})


