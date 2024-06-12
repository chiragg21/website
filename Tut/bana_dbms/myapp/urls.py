from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [ 
   # path('', views.main, name='main'),
   path('', views.fabric_query, name='fabric_query'),
   path('fabrics/inventory/', views.fabric_inventory, name='fabric_inventory'),
   path('fabrics/', views.fabric_list, name='fabric_list'),
]
