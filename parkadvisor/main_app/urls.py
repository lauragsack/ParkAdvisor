from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks_index, name='index'),
    path('about/', views.about, name='about'),
    path('parks/<int:park_id>/', views.parks_detail, name='detail'),
    path('parks/<int:park_id>/add_review', views.add_review, name='add_review'),
    path('reviews/<int:review_id>', views.reviews_update, name='reviews_update'),
    path('reviews/<int:review_id>', views.reviews_delete, name='reviews_delete'),
     # should review cards on reviews index html have edit and delete buttons?
    path('reviews/', views.reviews_index, name='reviews_index'),
    # path('reviews/', views.reviews_index, name='reviews_detail'),

    # todo not sure if we need assoc_review path for one-to-many (added for many-to-many in cats)
    # path('parks/<int:park_id>/assoc_review/<int:review_id>/', views.assoc_review, name='assoc_review'),

    # todo: if we use CBVs, rename reviews template directory to main_app
    # if we don't use CBVs, delete these paths
    # path('reviews/', views.ReviewList.as_view(), name='reviews_index'),
    # path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='reviews_detail'),
    # path('reviews/create/', views.ReviewCreate.as_view(), name='reviews_create'),
    # path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
    # path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete')
    path('accounts/signup', views.signup, name='signup'),
]