from django.urls import path, include # type: ignore
from . import views
from .views import EmpresaViewSet, EmpleadoViewSet, CalculosViewSet, NovedadesViewSet
from rest_framework.routers import DefaultRouter # type: ignore


empresa_router = DefaultRouter()
empresa_router.register(r'empresarest', EmpresaViewSet)

empleado_router = DefaultRouter()
empleado_router.register(r'empleadorest', EmpleadoViewSet)

calculos_router = DefaultRouter()
calculos_router.register(r'calculorest', CalculosViewSet)

novedades_router = DefaultRouter()
novedades_router.register(r'calculorest', NovedadesViewSet)


urlpatterns = [
    path('empresa',include(empresa_router.urls)),
    path('empleado',include(empleado_router.urls)),
    path('calculosdepe',include(calculos_router.urls)),
    path('novedadesdepe',include(novedades_router.urls)),
 

    #Gestion de Calculos
    path('calcular/<int:numero_identificacion>/', views.CalculosGenerales.calcularSalario, name='calcularemple'),
    path('registro_novedades/<int:numero_identificacion>/', views.CalculosGenerales.registroNovedades, name='registroNovedades'),
    path('calculos/<str:documento>/<str:fecha>/', views.CalculosGenerales.HistorialNomina, name='verNomina'),
    path('todos_los_calculos<int:numero_identificacion>/', views.CalculosGenerales.obtener_todos_los_calculos, name='todos_los_calculos'),



]