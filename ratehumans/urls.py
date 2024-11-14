from django.contrib import admin
from django.urls import path, include
from ratings import views as ratings_views
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView

urlpatterns = [
    path("", include('ratings.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/google/', OAuth2LoginView.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')),  # Google login URLs
]
