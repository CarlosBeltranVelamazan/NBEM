# Descomprime todos los zip de las carpetas de las provincias y los deja en el sus respectivas carpetas de CCAA
import os
import pandas as pd
from zipfile import ZipFile

def Unzip (folder_download_INSPIRE_zips):
  print('Unzipping files')
  nombre_carpeta_base = folder_download_INSPIRE_zips
  with os.scandir(nombre_carpeta_base) as carpetas:
      for carpeta in carpetas: # carpeta es la carpeta de la CCAA
        if carpeta.is_dir():
            # Crea la carpeta de la CCAA donde guardar todos los archivos descomprimidos
            os.makedirs(nombre_carpeta_base + '\\' + carpeta.name + r'\Unzipped', exist_ok=True)
            with os.scandir(nombre_carpeta_base + '\\' + carpeta.name) as subcarpetas:
                for subcarpeta in subcarpetas: # subcarpeta es la carpeta de la Provincia
                  if subcarpeta.is_dir():
                    if subcarpeta.name == r'Unzipped':
                      pass
                    else:
                      with os.scandir(subcarpeta) as ficheros: # los .zip a descomprimir
                        for fichero in ficheros:
                          # Selecciona el archivo a descomprimir
                          with ZipFile (nombre_carpeta_base + '\\' + carpeta.name + '\\' + subcarpeta.name + '\\' + fichero.name, 'r') as zObject:
                            # Descomprime el archivo en esa ubicación
                            zObject.extractall(path=nombre_carpeta_base + '\\' + carpeta.name + r'\Unzipped')
                  else:
                        # Selecciona el archivo a descomprimir
                        with ZipFile (nombre_carpeta_base + '\\' + carpeta.name + '\\' + subcarpeta.name, 'r') as zObject:
                          # Descomprime el archivo en esa ubicación
                          zObject.extractall(path=nombre_carpeta_base + '\\' + carpeta.name + r'\Unzipped')
        else:
          pass

