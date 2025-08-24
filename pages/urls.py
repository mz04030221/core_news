from django.urls import path

from pages.views import HomePageView, AboutPageView, ProfilePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
]
