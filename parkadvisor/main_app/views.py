from django.shortcuts import render, redirect
from .models import Park, Review, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# todo delete below line if go with CBVs
from .forms import ReviewForm

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

# def assoc_review(request, park_id, review_id):
#     Park.objects.get(id=park_id).reviews.add(review_id)
#     return redirect('detail', park_id=country_id)

def add_review(request, park_id):
    form = ReviewForm(request.POST)
    if form.is.valid():
        new_review = form.save(commit=False)
        new_review.park_id = park_id
        new_review.save()
    return redirect('detail', pard_id=park_id)

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

def reviews_delete(request, park_id, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('detail', park_id)



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
