import os
from xml.etree import ElementTree as ET
from django.shortcuts import render
from django.conf import settings

def load_data():
    # Ruta base del proyecto y construcción de rutas hacia los archivos XML y SQL
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    xml_path = os.path.join(BASE_DIR, 'full', 'et.xml')
    sql_path = os.path.join(BASE_DIR, 'comentariosaj', 'et_ComentariosAj.sql')

    # carga y analisis del archivo XML y obtiene la raíz del árbol XML para navegar por su contenido.
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Iteración sobre los elementos del bloque y extracción del contenido FormatUnit. Concatena en una cadena
    blocks = []
    for block in root.findall('block'):
        content = ''.join(el.text or '' for el in block.findall('formatUnit'))

        # Extracción del título del bloque del formatUnit
        title = None
        for format_unit in block.findall('formatUnit'):
            if format_unit.get('isTitle') == "true":
                title = format_unit.text
                break

        # Validar que el bloque tenga un título para incluirlo en el indice
        include_in_index = title is not None

        # Extraer atributos del formatUnit para crear un diccionario
        format_units = []
        for format_unit in block.findall('formatUnit'):
            attributes = {k: v for k, v in format_unit.attrib.items()}
            format_units.append(attributes)
        
        # Se extraen los valores específicos align, color, isBold del format_units
        align = format_units[0].get('align', 'justify') if format_units else 'justify'
        color = format_units[0].get('color', 'inherit') if format_units else 'inherit'
        is_bold = format_units[0].get('isBold', 'false') == "true" if format_units else False

        # Extraer imágenes asociadas
        images = [
            f"{settings.MEDIA_URL}{image.get('location')}"
            for image in block.findall('image') if image.get('location')
        ] + [
            f"{settings.MEDIA_URL}obj_{format_unit.get('image')}.gif"
            for format_unit in block.findall('formatUnit') if format_unit.get('image')
        ]

        # Agrega un diccionario con toda la información procesada del bloque a la lista blocks
        blocks.append({
            'id': block.get('id'),
            'order': block.get('order'),
            'content': content,  # Contenido completo del bloque
            'title': title,  # Título desde isTitle="true"
            'align': align,
            'color': color,
            'font_weight': 'bold' if is_bold else 'normal',
            'images': images,
            'comment': []  # Inicializar lista de comentarios
        })

    # Abrir y leer el archivo SQL
    try:
        with open(sql_path, 'r', encoding='utf-8') as file:
            sql_content = file.readlines()
    except FileNotFoundError:
        sql_content = []
        print(f"Error: El archivo {sql_path} no se encontró.")

    # Inicializa un diccionario para almacenar comentarios asociados a los bloques
    comments = {}
    for line in sql_content:
        if 'INSERT INTO' in line and '(' in line:
            try:
                values = line.split('VALUES', 1)[1].strip(' ();').split(',', maxsplit=6)
                block_id = values[1].strip("'").strip()
                # Extrae el texto del comentario
                if '<block' in values[6] and '</block>' in values[6]:
                    start_idx = values[6].find('<block')
                    end_idx = values[6].rfind('</block>') + len('</block>')
                    comment = values[6][start_idx:end_idx].strip()
                else:
                    comment = values[6].strip("'").strip()
                
                # Asocia el comentario al bloque correspondiente en el diccionario
                if block_id not in comments:
                    comments[block_id] = []
                comments[block_id].append(comment)
            except IndexError:
                continue  # Saltar líneas mal formadas

    # Une los comentarios procesados con los bloques correspondientes
    for block in blocks:
        block['comment'] = comments.get(block['id'], [])

    return blocks

# Llama a load_data para procesar bloques y comentarios y pasa los bloques como contexto a la plantilla base.html.
def home(request):
    blocks = load_data()
    context = {
        'blocks': blocks,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'base.html', context)