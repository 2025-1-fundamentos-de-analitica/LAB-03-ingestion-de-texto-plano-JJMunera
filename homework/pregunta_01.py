"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", 'r', encoding='utf-8') as f:
        lineas = [line.rstrip() for line in f if line.strip() and not re.match(r'^-+$', line.strip())]

    datos = []
    i = 0
    while i < len(lineas):
        linea = lineas[i]

        if re.match(r'^\s*\d+', linea):
            partes = re.split(r'\s{2,}', linea.strip(), maxsplit=3)
            cluster = int(partes[0])
            cantidad = int(partes[1])
            porcentaje = float(partes[2].replace(',', '.').replace('%', '').strip())
            palabras = partes[3] if len(partes) > 3 else ''
            
            i += 1
            while i < len(lineas) and not re.match(r'^\s*\d+', lineas[i]):
                palabras += ' ' + lineas[i].strip()
                i += 1
            
            # Normalizar: un solo espacio después de cada coma
            palabras = re.sub(r'\s+', ' ', palabras)                      # Múltiples espacios a uno
            palabras = re.sub(r'\s*,\s*', ', ', palabras)                # Comas limpias
            palabras = palabras.strip().rstrip(',')

            datos.append({
                'cluster': cluster,
                'cantidad_de_palabras_clave': cantidad,
                'porcentaje_de_palabras_clave': porcentaje,
                'principales_palabras_clave': palabras
            })
        else:
            i += 1

    return pd.DataFrame(datos)



    """
      
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
