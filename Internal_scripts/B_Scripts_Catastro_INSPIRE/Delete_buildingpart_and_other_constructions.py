# Para aligerar el peso de los archivos (todos los edificios de España comprimidos en .zip son 5 gb, descomprimidos son 150 gb incluyendo capa buildings, buildingsparts y other constructions)
# eliminamos las capas que no vamos a usar: buildingsparts y other constructions. Así es más sencillo trabajar y el peso es mucho menor. Quitando esas capas el peso es de 59 gb.
import os
import pandas as pd

def Delete_non_used_files (folder_download_INSPIRE_zips):
  print('Deleting unnecessary files (buildingpart, otherconstruction, and the XML)')
  nombre_carpeta_base = folder_download_INSPIRE_zips
  with os.scandir(nombre_carpeta_base) as carpetas:
      for carpeta in carpetas: # carpeta es la carpeta de la CCAA
        if carpeta.is_dir():
            with os.scandir(nombre_carpeta_base + '\\' + carpeta.name) as subcarpetas:
                for subcarpeta in subcarpetas: # subcarpeta es la carpeta de la Provincia
                  if subcarpeta.name == 'Unzipped':
                    with os.scandir(subcarpeta) as ficheros: # los .zip a descomprimir
                        for fichero in ficheros:
                          if fichero.name[-12:] == 'building.gml':    # Si quieres dejar los ficheros xml dejar al final este código: or fichero.name[-3:] == 'xml'
                              pass
                          else:
                        #      print (fichero.name[-12:])
                              os.remove(fichero)
                  else:
                    pass
        else:
          pass
