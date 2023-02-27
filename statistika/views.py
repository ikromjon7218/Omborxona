from django.shortcuts import render, redirect
from django.views import View
from .models import *

class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {'statistics': Statistika.objects.filter(ombor__user=request.user),
                    'clientlar' : Client.objects.all(),
                    'mahsulotlar': Mahsulot.objects.all()}
            return render(request, 'stats.html', data)
        return redirect('/')
    def post(self, request):
        Statistika.objects.create(
            mahsulot=Mahsulot.objects.get(id=request.POST.get('pr')),
            client=Client.objects.get(id=request.POST.get('client')),
            miqdor=request.POST.get('miqdor'),
            narx=request.POST.get('summa'),
            tolandi=request.POST.get('tolandi'),
            qarz=request.POST.get('nasiya'),
            ombor=Ombor.objects.get(user=request.user),)
        m = Mahsulot.objects.get(id=request.POST.get('pr'))
        m.miqdor = int(m.miqdor) - int(request.POST.get('miqdor'))
        m.save()
        cl = Client.objects.get(id=request.POST.get('client'))
        
        return redirect('/stats/')