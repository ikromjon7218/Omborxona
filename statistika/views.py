from django.shortcuts import render, redirect
from django.views import View
from .models import *
from asosiy.models import *

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

class StatEditView(View):
    def post(self, request, son):
        Statistika.objects.filter(id=son).update(mahsulot=Mahsulot.objects.get(request.POST.get('m')),
                client=Client.objects.get(request.POST.get('c')),
                miqdor=request.POST.get('miqdor'),
                sana=request.POST.get('sana'),
                narx=request.POST.get('narx'),
                tolandi=request.POST.get('tolandi'),
                qarz=request.POST.get('qarz'),
                ombor=Ombor.objects.get(request.POST.get('o')))
        return redirect('/stats/')
    def get(self, request, son):
        data = {"stat": Statistika.objects.get(id=son)}
        return render(request, "stat_edit.html", data)

class StatDeleteView(View):
    def get(self, request, son):
        if Statistika.objects.get(id=son).ombor.user == request.user:
            Statistika.objects.get(id=son).delete()
        return redirect('/stats/')