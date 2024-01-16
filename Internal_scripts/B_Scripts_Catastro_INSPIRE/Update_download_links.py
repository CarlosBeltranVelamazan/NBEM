# El texto es el copiado de la base ATOM del Catastro INSPIRE, este script quita el texto que sobre de cada txt y deja el link para descargar al capa Buildings de cada munciipio de esa provincia. Y pone un texto al principio que es para ejecutarlo correctamente en cmd

def Automate_links (folder_read_files, folder_save_files, encoding_txt):
      import os
      import pandas as pd

      os.makedirs(folder_save_files, exist_ok=True)
      nombre_carpeta_guardar = folder_save_files

      nombre_carpeta = folder_read_files

      # Este archivo me dirá cuantos archivos tienen que descargarse por provincia
      Num_archivos = pd.DataFrame(columns=('Province', 'Number of files'))

      with os.scandir(nombre_carpeta) as ficheros:
            for fichero in ficheros:
            #     print(fichero.name)
                  df = pd.read_csv(nombre_carpeta + '\\' + fichero.name, sep=".zip", header=None, engine='python', encoding=encoding_txt)
                  sepcol = df.pop (0)
            #      print (sepcol)
            #      sepcol = sepcol.str.replace(" ", "%20").astype(float,errors='ignore')
            #      sepcols = 'start ' + sepcol.astype(str) + '.zip'
                  sepcols = sepcol.astype(str) + '.zip'
                  a = sepcols.shape[0]
            #      encabezado = pd.Series('@echo off') # Añade el comando para que sea ejecutable en cmd, si no se necesita basta con guardar como csv el DataFrame sepcols y quitarle la parte de start
            #      final = pd.Series(' ') # Cmd no saca la última fila, para ello dejo una vacía
                  encabezado = pd.Series()
                  encabezado = pd.concat([encabezado, sepcols], ignore_index=True)
            #      encabezado = pd.concat([encabezado, final], ignore_index=True)
                  encabezado.to_csv(nombre_carpeta_guardar + '\\' + fichero.name, header=None, index=False)
                  archivo = pd.DataFrame({'Province':[fichero.name[:-4]], 'Number of files':[a]})
                  Num_archivos = pd.concat([Num_archivos, archivo], axis=0)

      Num_archivos.to_excel(nombre_carpeta_guardar + r"\Number_of_INSPIRE_files_per_region.xlsx", index=False)
      print ('The creation of download links is complete')

if __name__ == "__main__":
      folder_read_files = r'INSPIRE_cadastre\Original_txt_links'
      folder_save_files = r'INSPIRE_cadastre\Automated_links'
      Automate_links (folder_read_files, folder_save_files)

