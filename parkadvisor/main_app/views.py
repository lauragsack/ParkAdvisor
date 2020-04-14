from django.shortcuts import render, redirect
from .models import Park, Review, User
from .forms import ReviewForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

#API RELATED
import requests, json


# Create your views here.
def landing(request):
    
    return render(request, 'landing.html')

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
    park_id = review.park.id
    if request.method == 'GET':
        review.likes += 1
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

@user_passes_test(lambda u: u.is_superuser)
def external_api(request):
    url = 'https://developer.nps.gov/api/v1/parks?limit=50&api_key=65cD2Pey6zgKAXKmKA71wA6sHmuIcsAdiSs5xmhp'
    response = requests.get(url)
    data = response.json()
    for park in data["data"]:
        try:
            phoneNum = park["contacts"]["phoneNumbers"][0]["phoneNumber"]
            formatedPhoneNum = ("("+phoneNum[:3]+")-"+phoneNum[3:6]+"-"+phoneNum[6:])

            formated_address = park["addresses"][0]["line1"] + ", " + park["addresses"][0]["city"] + ", " + park["addresses"][0]["stateCode"] +" " + park["addresses"][0]["postalCode"]
            if( (not(Park.objects.filter(name=park["fullName"]).exists())) and (park["designation"] == "National Park") ):
                new_park = Park.objects.create(name=park["fullName"], location=formated_address,entrance_fee=int(float(park["entranceFees"][0]["cost"])), description=park["description"], phone=formatedPhoneNum, website=park["url"], image=park["images"][0]["url"], avg_rating=3.6)
        except:
            continue
    return render(request, 'parks/external_api.html', {'data': data})


