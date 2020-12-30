from django.urls import path

from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('gesla/', views.gesla, name='gesla'),
            path('snezak/', views.snezak, name='snezak'),
            path('snezinka/', views.snezinka, name='snezinka'),
            path('jelencek/', views.jelencek, name='jelencek'),
            path('sani/', views.sani, name='sani'),
            path('lucke/', views.lucke, name='lucke'),
            path('kraguljcki/', views.kraguljcki, name='kraguljcki'),
            path('snezena_kepa/', views.snezena_kepa, name='snezena_kepa'),
            path('mraz/', views.mraz, name='mraz'),
            path('sneg/', views.sneg, name='sneg'),
            path('rezultati/', views.rezultati, name='rezultati'),
        ]
