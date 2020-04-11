from django.shortcuts import render, redirect
from .models import Park, Review, User
# todo: delete below line if go with CBVs
from .forms import ReviewForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

###### TEMP DATA ######
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
###### TEMP DATA ######

# Create your views here.
def home(request):
    return redirect(request, 'parks/')

def about(request):
    return render(request, 'about.html')

def parks_index(request):
    return render(request, 'parks/index.html', { 'cats': cats })

def parks_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    review_form = ReviewForm()
    this_parks_reviews = park.review_set.all()
    return render (request, 'parks/detail.html', {
        'park': park,
        'review_form': review_form,
        'reviews': this_parks_reviews
    })

# todo: do we need this?
# def assoc_review(request, park_id, review_id):
#     Park.objects.get(id=park_id).reviews.add(review_id)
#     return redirect('detail', park_id=country_id)

@login_required
def add_review(request, park_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.park_id = park_id
            review.user = request.user
            new_review.save()
            return redirect('detail', pard_id=park_id)
    else:
        form = ReviewForm()
        context = { 'form': form }
    return render(request, 'reviews/review_form.html', context)

# todo: do we need @login_required or can we only display edit b utton if review.user=request.user?
def reviews_update(request, park_id, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('detail', park_id)
    else: 
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', { 'form': form })

# todo do we need @login_required? or can we only display delete button if review.user=request.user?
def reviews_delete(request, park_id, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('detail', park_id)

# todo: add to logged in navbar
@login_required
def reviews_index(request, review):
    reviews = request.user.reviews_set.all()
    return render(request, 'reviews/review_list.html', { 'cats': cats })


# todo add this to base html nav: <li><a href="{% url 'signup' %}">Sign Up</a></li>
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



# class ReviewList(ListView):
#     model = Review

# class ReviewDetail(DetailView):
#     model = Review

# class ReviewCreate(LoginRequiredMixin, CreateView):
#     model = Review
#     fields = '__all__'

# class ReviewUpdate(LoginRequiredMixin, UpdateView):
#     model = Review
#     fields = '__all__'

# class ReviewDelete(LoginRequiredMixin, DeleteView):
#     model = Review
#     success_url = '/parks/index.html/'
