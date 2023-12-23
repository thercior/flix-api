from django.urls import path
from reviews.views import *

app_name = 'Reviews'

urlpatterns = [
    path('reviews/', ReviewCreateListView.as_view(), name='reviews_create_list'),
    path('reviews/<pk>/', ReviewDetailUpdateDeleteView.as_view(), name='reviews_detalhes'),
    
]
