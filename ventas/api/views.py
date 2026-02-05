from rest_framework import viewsets
from ventas.models import Empresas, Marcas, Sucursales, Ventas
from ventas.api.serializers import (
    EmpresasSerializer,
    MarcasSerializer,
    SucursalesSerializer,
    VentasSerializer,
    VentasConRelacionesSerializer
    )

# from kfc.models import Ventas
# from kfc.api.serializers import VentasSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class MarcasViewSet(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer

class SucursalesViewSet(viewsets.ModelViewSet):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalesSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

# joins
class VentasConRelacionesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VentasConRelacionesSerializer
    
    def get_queryset(self):
        # Obtenemos los IDs de sucursales que realmente existen
        sucursales_existentes = Sucursales.objects.values_list('id_sucursal', flat=True)
        # Filtramos solo ventas con sucursales existentes para evitar errores de integridad
        return Ventas.objects.select_related(
            'id_sucursal__id_marca__id_empresa'
        ).filter(id_sucursal__in=sucursales_existentes)

