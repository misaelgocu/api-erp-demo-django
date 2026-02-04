from rest_framework import serializers, viewsets
from ventas.models import  Empresas, Marcas, Sucursales, Ventas


class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'

class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'

class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        fields = '__all__'

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'

# joins
class MarcasConEmpresaSerializer(serializers.ModelSerializer):
    empresa = EmpresasSerializer(source='id_empresa', read_only=True)
    
    class Meta:
        model = Marcas
        fields = ['id_marca', 'nombre_marca', 'empresa', 'created_at', 'updated_at']


class SucursalesConMarcaSerializer(serializers.ModelSerializer):
    marca = MarcasConEmpresaSerializer(source='id_marca', read_only=True)
    
    class Meta:
        model = Sucursales
        fields = ['id_sucursal', 'cc_suc', 'nombre_sucursal', 'marca', 'created_at']


class VentasConRelacionesSerializer(serializers.ModelSerializer):
    sucursal = SucursalesConMarcaSerializer(source='id_sucursal', read_only=True)
    
    class Meta:
        model = Ventas
        fields = ['id_dft', 'fecha', 'vtas_netas', 'sucursal', 'periodo']