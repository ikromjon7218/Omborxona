from django.urls import path
from .views import *

urlpatterns = [
    path('', StatistikaView.as_view()),
    path('edit/<int:son>/', StatEditView.as_view()),
    path('delete/<int:son>/', StatDeleteView.as_view()),

]