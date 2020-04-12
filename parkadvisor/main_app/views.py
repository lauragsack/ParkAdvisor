from django.shortcuts import render, redirect
from .models import Park, Review, User
# todo: delete below line if go with CBVs
from .forms import ReviewForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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

# todo: do we need this?
# def assoc_review(request, park_id, review_id):
#     Park.objects.get(id=park_id).reviews.add(review_id)
#     return redirect('detail', park_id=country_id)

@login_required
def add_review(request, park_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
      new_review = form.save(commit=False)
      new_review.park_id = park_id
      review.user = request.user
      new_review.save()
    return redirect('detail', park_id=park_id)

# @login_required
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

# @login_required
def reviews_delete(request, review_id):
    print("review_id", review_id)
    park_id = review.park.id
    print("park_id", park_id)
    Review.objects.get(id=review_id).delete()
    return redirect('detail', park_id)

# todo: add to logged in navbar
@login_required
def reviews_index(request):
    reviews = Review.objects.filter(user=request.user)
    return render(request, 'reviews/review_list.html', { 'reviews': reviews })

# def reviews_detail(request, review_id):
#     review = Review.objects.get(id=review_id)
#     review_form = ReviewForm()
#     return render (request, 'parks/detail.html', {
#         'park': park,
#         'review_form': review_form
#     })


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
