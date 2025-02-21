from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/create', views.createReview, name='createReview'),
    path('reviews/<int:review_id>', views.updatereview, name='updatereview'),
    path('reviews/<int:review_id>/delete', views.deletereview, name='deletereview'),

]