from django.urls import path
from .views import (
    ProfileListCreateAPIView,
    ProfileListAPIView,
    ProfileDetailAPIView,
    ProfileUpdateAPIView,
    ProfileDeleteAPIView,
    profile_form_page
)

urlpatterns = [
    path('add/', ProfileListCreateAPIView.as_view(), name='addAPI'),
    path('', ProfileListAPIView.as_view(), name='checkAPI'),
    path('api/<int:pk>/', ProfileDetailAPIView.as_view(), name='profile-detail'),  # GET single
    path('api/<int:pk>/update/', ProfileUpdateAPIView.as_view(), name='profile-update'),  # PUT/PATCH
    path('api/<int:pk>/delete/', ProfileDeleteAPIView.as_view(), name='profile-delete'),  # DELETE
    path('profile/', profile_form_page, name='profile-form-page'),
]