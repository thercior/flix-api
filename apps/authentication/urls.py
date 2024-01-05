from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = 'Authentication'

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
