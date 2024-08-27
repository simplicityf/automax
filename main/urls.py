from django.urls import path

from .views import main_view, home_view, list_view, listing_view, edit_view

urlpatterns = [
    path ('', main_view, name='main'),
    path ('home/', home_view, name='home'),
    path ('list/', list_view, name='list'),
    path ('listing/<str:id>/', listing_view, name='listing'),
    path ('edit/<str:id>/edit/', edit_view, name='edit'),
]
