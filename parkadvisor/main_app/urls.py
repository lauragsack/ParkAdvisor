from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks_index, name ='index'),
    path('about/', views.about, name='about'),
    path('parks/<int:park_id>/', views.parks_detail, name='detail'),
    # path('parks/<int:park_id>/add_review', views.add_review, name='add_review'),
    # path('parks/<int:park_id>/assoc_review/<int:review_id>/', views.assoc_review, name='assoc_review'),
    # path('reviews/', views.ReviewList.as_view(), name='reviews_index'),
    # path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='reviews_detail'),
    # path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
    # path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete')
]