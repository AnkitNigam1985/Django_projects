from django.urls import path,re_path

from . import views
#from .views import ElectronicsView
#from .views import ElectronicsView2
#from .views import ElectronicsView3
from .views import EquipmentView

urlpatterns = [
    path('', views.index, name='index'),
    #path('1', views.detail, name='detail')
    re_path(r'^\d+', views.detail, name='detail'),
    re_path(r'^electronics', views.electronics, name='electronics'),
    re_path(r'^logout', views.logout, name='logout'),
    #re_path(r'^electronics', ElectronicsView.as_view(), name='electronics'),
    #re_path(r'^electronics', EquipmentView.as_view(), name='electronics'),
    #re_path(r'^electronics', ElectronicsView2.as_view(), name='electronics'),
    #re_path(r'^electronics', ElectronicsView3.as_view(), name='electronics'),
]