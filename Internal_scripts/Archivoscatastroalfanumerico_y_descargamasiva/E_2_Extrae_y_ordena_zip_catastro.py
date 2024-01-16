# La consulta al catastro alfanumerico te devuelve un archivo zip con muchos zip dentro con los .CAT con muchisima información
# El script descomprime todos los zip de las carpetas de las provincias y los deja en el sus respectivas carpetas de CCAA y la ordena en carpetas para poder trabajarla de forma ordenada

import os
import pandas as pd
from zipfile import ZipFile
import gzip
import shutil
from time import time


def Extraer_CAT (Carpeta_archivos_descargas_CA):

    # Para saber cuánto tarda este proceso
    inicio  = time()


    carpeta_base = Carpeta_archivos_descargas_CA                # La carpeta donde están los .zip del catastro
    nombre_carpeta = Carpeta_archivos_descargas_CA + '\\' + 'Archivos_descomprimidos'                                # La carpeta donde estará una carpeta por provincia con los datos extraidos (formato .CAT)
 #   nombre_carpeta_guardar = nombre_carpeta + '\\Datos_tratados_por_Provincia'                                      # No es necesaira. La carpeta donde estarán los datos ya tratados por provincia (formato csv o parquet)

    os.makedirs(nombre_carpeta, exist_ok=True)
 #   os.makedirs(nombre_carpeta_guardar, exist_ok=True)

    with os.scandir(carpeta_base) as ficheros:
        for fichero in ficheros:          
            if fichero.name[-4:] == '.zip':                                                                                         # Si el fichero es un zip funciona si no se lo salta, así elimino posibles carpetas, txt o cualquier cosa que pudiera acabar ahí y ser un problema
                os.makedirs(nombre_carpeta, exist_ok=True)
                with ZipFile (carpeta_base + '\\' + fichero.name, 'r') as zObject:                                                  # Esta línea y la siguiente extraen los archivos del .zip
                    zObject.extractall(nombre_carpeta)
                with os.scandir(nombre_carpeta + '\\' + fichero.name[:-4]) as subficheros:                                          # Esta línea busca los archivos en la nueva carpeta creada al extraer
                    for subfichero in subficheros:
                        with open(nombre_carpeta + '\\' + fichero.name[:-4] + '\\' + subfichero.name[:-3], 'wb') as fout:           # Esta línea y las siguientes extraen los archivos del .gz
                            with gzip.open(nombre_carpeta + '\\' + fichero.name[:-4] + '\\' + subfichero.name, 'rb') as fin:
                                shutil.copyfileobj(fin,fout)                                                                        # IMPORTANTE: Si donde vamos a extraer el gz ya hay un archivo que se llama así da error esta línea, borrar el archivo que ibamos a sobreescribir y listo
                with os.scandir(nombre_carpeta + '\\' + fichero.name[:-4]) as subficheros:                                          # Este bucle es para eliminar los archivos descomprimidos, así reducimos peso que son muchisimos
                    for subfichero in subficheros:
                        if subfichero.name[-3:] == '.gz':
                            os.remove(subfichero)            

    # Para conocer cuánto tarda el proceso
    duracion = (time() - inicio)/60
    with open(Carpeta_archivos_descargas_CA + '\\' + r"Duración_proceso_E_2" + ".txt", 'w') as f:
                    f.write('Realizar todo el proceso E_2 de descomprimir los archivos zip del catastro ha tardado ' + str(duracion) + ' minutos' )

    print ('Terminado')
