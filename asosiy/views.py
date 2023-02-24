from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.views import View

class LoginView(View):
    def post(self, request):
        foydalanuvchi = authenticate(username=request.POST.get('l'), password=request.POST.get('p'))
        if foydalanuvchi:
            return redirect('/bolim')
        login(request, foydalanuvchi)
        return redirect('/')
    def get(self, request):
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class BolimView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

class MahsulotlarView(View):
    def get(self, request):
        ombor1 = Ombor.objects.get(user=request.user)
        data = {"mahsulotlar": Mahsulot.objects.filter(ombor=ombor1)}
        return render(request, 'products.html', data)

    def post(self, request):
        Mahsulot.objects.create(
            nom=request.POST.get('pr_name'),
            brend=request.POST.get('pr_brend'),
            narx=request.POST.get('pr_price'),
            kelgan_sana=request.POST.get('pr_date'),
            miqdor=request.POST.get('pr_amount'),
            olchov=request.POST.get('pr_olchov'),
            ombor=Ombor.objects.get(user=request.user),)
        return redirect('/asosiy/mahsulotlar/')

class Mahsulot_DeleteView(View):
    def get(self, request, son):
        mah = Mahsulot.objects.get(id=son)
        if Ombor.objects.get(user=request.user) == mah.ombor:
            mah.delete()
        return redirect('/asosiy/mahsulotlar/')

class Mahsulot_EditView(View):
    def get(self, request, son):
        mahsulot = Mahsulot.objects.get(id=son)
        if mahsulot.ombor == Ombor.objects.get(user=request.user):
            data = {
                "product": mahsulot
            }
            return render(request, 'product_update.html', data)
        return redirect('/asosiy/mahsulotlar/')

    def post(self, request, son):
        mah = Mahsulot.objects.filter(id=son)
        if Ombor.objects.get(user=request.user) == mah.ombor:
            mah.update(
                narx = request.POST.get('price'),
                miqdor = request.POST.get('amount'),)
        data = {"product": Mahsulot.objects.get(id=son)}
        return render(request, "product_update.html", data)

class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')

class ClientsView(View):
    def get(self, request):
        ombor1 = Ombor.objects.get(user=request.user)
        data = {'clientlar': Client.objects.filter(ombor=ombor1)}
        return render(request, 'clients.html', data)
