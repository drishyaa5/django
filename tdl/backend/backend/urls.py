
from django.contrib import admin
from django.urls import path
from api.views import createUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", createUserView.as_view(), name="register"),
    papth("api/token/", TokenObtainPairView.as_view(), name="get_token")
]
