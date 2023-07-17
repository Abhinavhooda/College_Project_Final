from django.contrib.auth import views
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from core.views import *
from stations.views import *


urlpatterns = [
    path('', home, name='home'),
    path('chargingstations', chargingstations, name='chargingstations'),
    path('chargingstations/<slug:slug>/', stations, name='station'),
    path('about', about, name='about'),
    path('myaccount', My_account, name='myaccount'),
    path('offers', offers_view, name='offers'),
    path('helpline', helpline, name='helpline'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]