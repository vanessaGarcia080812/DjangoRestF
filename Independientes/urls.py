from django.urls import path, include # type: ignore
from . import views
from .views import IndependienteViewSet, CalculosViewSet
from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter

independiente_router = DefaultRouter()
independiente_router.register(r'independienterest', IndependienteViewSet)

calculos_router = DefaultRouter()
calculos_router.register(r'calculosrest', CalculosViewSet)


urlpatterns = [

    path('calcularinde/<str:numero_identificacion>/', views.CalculosGenerales.calcular_aportes, name='calcularinde'),

    
    
    
    path('inde',include(independiente_router.urls)),
    path('calcu',include(calculos_router.urls)),
 
 
]