from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status# type: ignore
from rest_framework import viewsets# type: ignore
from . serializer import IndependienteSerializer, CalculosSerializer
from . models import Independiente, Calculos,DatosCalculos

from django.shortcuts import render # type: ignore
from .forms import DatosCalculosForm
from django.http import HttpRequest # type: ignore




class IndependienteViewSet(viewsets.ModelViewSet):
    queryset=Independiente.objects.all()
    serializer_class=IndependienteSerializer

class IndependienteCreate(APIView):
    def post(self, request, format=None):
        serializer = IndependienteViewSet(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalculosViewSet(viewsets.ModelViewSet):
    queryset=Calculos.objects.all()
    serializer_class=CalculosSerializer



class CalculosGenerales(HttpRequest):
    def calcular_aportes(request, numero_identificacion):
        
            independiente = Independiente.objects.get(pk=numero_identificacion)

# Busca la instancia de DatosCalculos relacionada con el independiente
            try:
                datos_calculos = DatosCalculos.objects.get(documento=independiente)
            except DatosCalculos.DoesNotExist:
                datos_calculos = None

            if request.method == 'POST':
                form = DatosCalculosForm(request.POST, instance=datos_calculos)
                if form.is_valid():
                    # Asigna la relación con independiente si es una nueva instancia
                    calculos = form.save(commit=False)
                    if datos_calculos is None:
                        calculos.documento = independiente
                    calculos.save()
                    # Aquí puedes redirigir a otra página o renderizar una respuesta
          
                datos_calculos=DatosCalculos.objects.filter(documento=independiente)#esto es para traer los datos                 
                
                for objeto in datos_calculos:
                    
                    salario_base = objeto.salarioBase
                    nivel_arl = objeto.arl
                    ccf = objeto.CCF
                    porcentaje_ibc=objeto.ibc
                    
                
                ibc = salario_base * (porcentaje_ibc/100)
                if ibc<1300000:
                    ibc=1300000
                    
                salud = ibc * 0.125
                pension = ibc * 0.16
                
                
             
                # fsp =fsp
            
                arl = CalculosGenerales.calcular_arl (ibc,nivel_arl)
                
                
                if ccf == 'Si':
                    ccf = ibc * 0.04
                else:
                    ccf = 0
                
                salud = salud
                pension = pension
                # fsp = fsp
                
                context = {
                    'independiente': independiente,
                    'salario_base': salario_base,
                    'ibc': ibc,
                    'salud': salud,
                    'pension': pension,
                    'arl': arl,
                    'ccf': ccf,
                    # 'fsp': fsp
                }
                
                return render(request, 'independientes/resultado_calculos.html', context)
            
            
            else:
                form = DatosCalculosForm()
        
            return render(request, 'independientes/calcular_aportes.html', {'form': form, 'independiente': independiente})
    


    def calcular_arl(ibc, arl_nivel):
        
        if arl_nivel == '1':
                arl = ibc * 0.00522
        elif arl_nivel == '2':
                arl = ibc * 0.01044
        elif arl_nivel == '3':
                arl = ibc * 0.02436
        elif arl_nivel == '4':
                arl = ibc * 0.04350
        elif arl_nivel == '5':
                arl = ibc * 0.06960
        elif arl_nivel == '0':
                arl = 0
        return (arl)
        

