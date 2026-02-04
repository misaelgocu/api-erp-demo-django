# 🚀 Comandos para Iniciar tu Proyecto

## 📦 Instalación Inicial

### 1. Navegar al proyecto
```bash
cd /home/misael/Works/Python_prokects/API_erp_demo/erp
```

### 2. Activar entorno virtual
```bash
source ../venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🗄️ Configurar Base de Datos

### 4. Aplicar migraciones (crea db.sqlite3 automáticamente)
```bash
python manage.py migrate
```

### 5. Crear superusuario para el admin (opcional)
```bash
python manage.py createsuperuser
```

## ▶️ Iniciar Servidor

### 6. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```

Accede a:
- API: http://127.0.0.1:8000/api/
- Documentación Swagger: http://127.0.0.1:8000/docs/
- Admin: http://127.0.0.1:8000/admin/

## 🔄 Git (Opcional pero Recomendado)

### Inicializar repositorio
```bash
git init
git add .
git commit -m "Initial commit"
```

### Conectar con GitHub (si tienes repo remoto)
```bash
git remote add origin https://github.com/tu-usuario/tu-repo.git
git branch -M main
git push -u origin main
```

## 🧪 Comandos Útiles para Desarrollo

### Ver estructura de la base de datos
```bash
python manage.py dbshell
.tables
.schema ventas_empresas
.exit
```

### Crear datos de prueba desde el shell
```bash
python manage.py shell
```

Luego en el shell de Python:
```python
from ventas.models import Empresas, Marcas

# Crear empresa
empresa = Empresas.objects.create(
    nombre_empresa="Mi Empresa Test",
    created_at="2024-01-01",
    updated_at="2024-01-01"
)

# Ver todas las empresas
Empresas.objects.all()

# Salir
exit()
```

### Limpiar base de datos (si quieres empezar de cero)
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📝 Resumen de Archivos Agregados

Los archivos que se crearon en tu proyecto:

- `.gitignore` - Archivos que Git debe ignorar
- `requirements.txt` - Dependencias del proyecto
- `README.md` - Documentación completa del proyecto
- `COMANDOS.md` - Este archivo con comandos útiles

## ⚠️ Archivos NO Modificados

Tu código original NO fue modificado:
- `kfc/settings.py` - Sin cambios
- `ventas/models.py` - Sin cambios  
- `ventas/api/` - Sin cambios
- Todos los demás archivos permanecen intactos

## 🌐 Para Desplegar en PythonAnywhere

Cuando estés listo para desplegar, consulta la sección "Despliegue en PythonAnywhere" del README.md

Pasos básicos:
1. Sube tu código a GitHub
2. Clona en PythonAnywhere
3. Crea virtualenv e instala dependencias
4. Ejecuta migraciones
5. Configura Web App
6. Edita WSGI
7. Configura static files
8. Actualiza settings.py
9. Reload

---

**¡Tu proyecto está listo para desarrollar! 🎉**
