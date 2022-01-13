from django.contrib import admin
from django.urls import path, include
from .views import BookingCreateView, BookingDetailView, BookingListView

urlpatterns = [
    path('create/', BookingCreateView.as_view()),
    path('detail/<int:pk>/', BookingDetailView.as_view()),
    path('all/', BookingListView.as_view()),
]
