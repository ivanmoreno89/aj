
# Prueba Técnica - Avance Jurídico S.A.S

Este proyecto es una prueba técnica desarrollada con Django. El objetivo es demostrar habilidades de desarrollo en backend, frontend y manipulación de datos estructurados y multimedia.

## Descripción

El sistema permite la visualización y gestión de bloques de contenido extraídos de un archivo XML (`et.xml`) y comentarios asociados desde un archivo SQL (`et_ComentariosAj.sql`). Además, los bloques pueden incluir imágenes referenciadas en formato GIF. Se incluyen funcionalidades como:

- **Visualización de bloques con atributos y formato.**
- **Búsqueda y filtrado interactivo.**
- **Gestión de comentarios asociados a cada bloque.**
- **Visualización de imágenes relacionadas.**

## Tecnologías Utilizadas

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Base de Datos**: SQLite
- **Archivos Multimedia**: Imágenes en formato GIF
- **Otros**: XML, SQL

## Requisitos del Sistema

- Python 3.8+
- Django 4.2.16
- Entorno virtual de Python recomendado
- Navegador moderno para la interfaz de usuario

## Estructura del Proyecto

```plaintext
aj/                         # Carpeta raíz del proyecto
├── aj/                     # Núcleo de la aplicación Django
│   ├── settings.py         # Configuración del proyecto
│   ├── urls.py             # Definición de rutas
│   ├── views.py            # Lógica para procesar bloques, imágenes y comentarios
│   └── ...
├── full/                   # Carpeta con el archivo XML para análisis
│   └── et.xml              # Datos estructurados en formato XML
├── comentariosaj/          # Comentarios asociados a los bloques
│   └── et_ComentariosAj.sql # Archivo SQL con comentarios
├── Imagenes/               # Carpeta con imágenes referenciadas
│   └── *.gif               # Archivos GIF
├── templates/              # Plantillas HTML
│   ├── base.html           # Estructura principal
│   ├── index.html          # Índice interactivo
│   ├── content.html        # Visualización de bloques y comentarios
│   └── ...
├── manage.py               # Script de gestión de Django
└── db.sqlite3              # Base de datos SQLite
```

## Próximas Mejoras

Estas son algunas posibles ideas para extender y mejorar el proyecto orientadas a agregar funcionalidad, optimización y usabilidad:

1. **Exportación de Datos**:
   - Permitir la exportación de bloques y comentarios a formatos como PDF.
   - Añadir botones en la interfaz para descargar un bloque del documento.

2. **Optimización del Rendimiento**:
   - Revisar y optimizar consultas a la base de datos.

3. **Diseño Responsivo Mejorado**:
   - Ajustar la interfaz para dispositivos móviles y tabletas.
   - Asegurar que todas las funcionalidades sean accesibles en pantallas pequeñas.

4. **Integración con APIs Externas**:
   - Permitir importar datos desde APIs externas o integrar servicios como Google Drive para cargar archivos.
