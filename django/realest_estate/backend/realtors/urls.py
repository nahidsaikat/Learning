from django.urls import path
from .views import RealtorListView, RealtorRetrieveView, TopSellerListView

urlpatterns = [
    path('', RealtorListView.as_view()),
    path('<pk>/', RealtorRetrieveView.as_view()),
    path('topseller/', TopSellerListView.as_view()),
]
