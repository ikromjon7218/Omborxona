from django.contrib import admin
from django.urls import path, include
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('bolim/', BolimView.as_view()),
    path('asosiy/', include('asosiy.urls')),
]
