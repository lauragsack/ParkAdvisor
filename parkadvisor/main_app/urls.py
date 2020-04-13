from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks_index, name='index'),
    path('about/', views.about, name='about'),
    path('parks/<int:park_id>/', views.parks_detail, name='detail'),
    path('parks/<int:park_id>/add_review', views.add_review, name='add_review'),
    path('reviews/update/<int:review_id>', views.reviews_update, name='reviews_update'),
    path('reviews/delete/<int:review_id>', views.reviews_delete, name='reviews_delete'),
    path('reviews/like/<int:review_id>', views.reviews_like, name='reviews_like'),
    path('reviews/', views.reviews_index, name='reviews_index'),
    path('accounts/signup', views.signup, name='signup'),
    path('external/api/', views.external_api, name='external_api'),
]