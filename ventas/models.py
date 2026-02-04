from django.db import models

class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(unique=True, max_length=150)
    
    # Campos de auditoría optimizados
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'empresas'
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre_empresa


class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    # Relación 1:N - Una marca pertenece a una empresa
    id_empresa = models.ForeignKey(
        Empresas, 
        on_delete=models.CASCADE, 
        db_column='id_empresa',
        related_name='marcas'
    )
    nombre_marca = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marcas'

    def __str__(self):
        return self.nombre_marca


class Sucursales(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    # Relación 1:N - Una sucursal pertenece a una marca
    id_marca = models.ForeignKey(
        Marcas, 
        on_delete=models.CASCADE, 
        db_column='id_marca',
        related_name='sucursales'
    )
    cc_suc = models.PositiveIntegerField(unique=True)
    compania = models.PositiveIntegerField()
    nombre_sucursal = models.CharField(max_length=100)
    
    # Según diagrama son INT, probablemente para timestamps o formatos YYYYMMDD
    fecha_inicio_suc = models.IntegerField(null=True, blank=True)
    fecha_fin_suc = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sucursales'
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return f"{self.cc_suc} - {self.nombre_sucursal}"


class Ventas(models.Model):
    # Usamos BigAutoField si prevemos millones de registros de ventas (escalabilidad)
    id_dft = models.BigIntegerField(primary_key=True)
    id_sucursal = models.ForeignKey(
        Sucursales, 
        on_delete=models.PROTECT, 
        db_column='id_sucursal',
        related_name='ventas'
    )
    fecha_dft = models.IntegerField()
    fecha = models.DateField()
    periodo = models.CharField(max_length=50, null=True, blank=True)
    semana = models.CharField(max_length=50, null=True, blank=True)
    
    # Parámetros Decimal ajustados para precisión financiera según la imagen
    vtas_netas = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    iva_comedor = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_iva_por_pagar = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    iva_llevar = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    descuentos = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    vtas_comedor = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    vtas_llevar = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    vtas_entrega = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    iva_entrega = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    iva_ventana = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    vtas_ventana = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    reembolso_cliente = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'ventas'
        # Indexación para mejorar rendimiento en búsquedas por fecha y sucursal
        indexes = [
            models.Index(fields=['fecha', 'id_sucursal']),
        ]

    def __str__(self):
        return f"Venta {self.id_dft} - {self.fecha}"