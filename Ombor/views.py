from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth import logout, login, authenticate
from .models import *

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        u = request.POST.get('login')
        p = request.POST.get('password')
        users = authenticate(request, username=u, password=p)
        if users is None:
            return redirect('login')
        else:
            login(request, users)
            return redirect("/bolim/")
class BolimView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

class RegView(View):
    def get(self, request):
        return render(request, 'register.html')

class ProductView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            p = Product.objects.filter(ombor=o)
            return render(request, "products.html", {'all_products': p})
        else:
            return redirect("login")
    def post(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            Product.objects.create(
                nom=request.POST.get('pr_name'),
                brend_nomi=request.POST.get('pr_brand'),
                narx=request.POST.get('pr_price'),
                miqdor=request.POST.get('pr_amount'),
                ombor=o,
            )
            return redirect('products')
        else:
            return redirect('login')
class Product_UpdateView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            product = Product.objects.get(id=son)
            return render(request, 'product_update.html', {'product': product})
        else:
            return redirect('login')
    def post(self, request, son):
        if request.user.is_authenticated:
            Product.objects.filter(id=son).update(
                nom=request.POST.get('pr_name'),
                brend_nomi=request.POST.get('pr_brand'),
                narx=request.POST.get('pr_price'),
                miqdor=request.POST.get('pr_amount'),
            )
            return redirect('products')
        else:
            return redirect("login")
class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            c = Client.objects.filter(ombor=o)
            return render(request, "clients.html", {'all_clients': c})
        else:
            return redirect("login")
    def post(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            Client.objects.create(
                ism=request.POST.get('client_name'),
                tel=request.POST.get('client_phone'),
                dokon_nomi=request.POST.get('client_shop'),
                joylashuv=request.POST.get('client_address'),
                qarz=request.POST.get('client_qarz'),
                ombor=o,
            )
            return redirect('clients')
        else:
            return redirect('login')


class Client_updateView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            c = Client.objects.get(id=son)
            return render(request, 'client_update.html', {'client': c})
        else:
            return redirect('login')
    def post(selfself, request, son):
        if request.user.is_authenticated:
            Client.objects.filter(id=son).update(
                ism=request.POST.get('client_name'),
                tel=request.POST.get('client_phone'),
                dokon_nomi=request.POST.get('client_shop'),
                joylashuv=request.POST.get('client_address'),
                qarz=request.POST.get('client_debt'),
            )
            return redirect('clients')
        else:
            return redirect('login')


def LogoutView(request):
    logout(request)
    return redirect('/')
def Del_pr(request, son):
    if request.user.is_authenticated:
        pr = Product.objects.get(id=son)
        pr.delete()
        return redirect('products')
    else:
        return redirect('login')
def Del_cl(request, son):
    if request.user.is_authenticated:
        cl = Client.objects.get(id=son)
        cl.delete()
        return redirect('clients')
    else:
        return redirect('login')
