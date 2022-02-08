from django.contrib import admin
from django.urls import path, include

from Ombor.views import Del_cl, Del_pr, Client_updateView, Product_UpdateView, ClientView, ProductView, \
    HomeView, LogoutView, BolimView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', BolimView.as_view(), name='bolim'),

    path('', HomeView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),

    path('products/', ProductView.as_view(), name='products'),
    path('clients/', ClientView.as_view(), name='clients'),

    path('product-update/<int:son>', Product_UpdateView.as_view(), name='product-update'),
    path('client-update/<int:son>', Client_updateView.as_view(), name='client-update'),

    path('delete_pr/<int:son>', Del_pr, name='delete_pr'),
    path('delete_cl/<int:son>', Del_cl, name='delete_cl'),

    path('stats/', include('Statistika.urls')),
    path('stat-update/<int:son>', include('Stat_UpdateStat.as_view()')),
    path('delete_st/<int:son>', include('Del_st')),
]
