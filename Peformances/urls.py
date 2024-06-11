from django.urls import path
from Peformances import views

urlpatterns = [
    path('peformances/', views.UserPeformanceListView.as_view()),
    path('peformances/<int:pk>/', views.UserPeformanceDetailListView.as_view()),
    path('events/', views.UserEventListView.as_view()),
    path('events/<int:pk>/', views.UserEventListDetailView.as_view()),
    
]
