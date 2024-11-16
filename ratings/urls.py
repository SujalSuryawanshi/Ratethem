from django.urls import path
from . import views

urlpatterns = [
    path('', views.swipe_page, name='swipe_page'),
    path('rate_human/', views.swipe_page, name='rate_human'),  # Add this line for AJAX handling
     path('submit-review/', views.submit_review, name='submit_review'),
     path('category/<str:category>/', views.category_view, name='category_view'),
     path('submit_human/', views.submit_human, name='submit_human'),
    path('review_humans/', views.review_humans, name='review_humans'),
    path('accept_human/<int:human_id>/', views.accept_human, name='accept_human'),
    path('reject_human/<int:human_id>/', views.reject_human, name='reject_human'),
    path('submission_success/', views.submission_success, name='submission_success'),
    path('search', views.search , name='search'),
    path("login", views.login_view, name="login")

]
