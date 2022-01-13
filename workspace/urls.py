from django.contrib import admin
from django.urls import path, include
from .views import WorkSpaceCreateView, WorkSpaceListView, WorkSpaceDetailView


app_name = 'workspace'
urlpatterns = [
    path('create/', WorkSpaceCreateView.as_view()),
    path('all/', WorkSpaceListView.as_view()),
    path('detail/<int:pk>/', WorkSpaceDetailView.as_view()),
]
