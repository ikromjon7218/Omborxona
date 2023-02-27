from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('bolim/', BolimView.as_view()),

    path('mahsulotlar/', MahsulotlarView.as_view()),
    path('mahsulot_delete/<int:son>/', Mahsulot_DeleteView.as_view()),
    path('mahsulot_edit/<int:son>/', Mahsulot_EditView.as_view()),


    path('clientlar/', ClientsView.as_view()),
    path('client_delete/<int:son>/', Client_DeleteView.as_view()),
    path('client_edit/<int:son>/', Client_EditView.as_view()),


]