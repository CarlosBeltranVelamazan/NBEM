 # Este script descarga los archivos desde las páginas webs que los aportan de cada CCAA
def Descargar (CCAA, Carpeta_archivos_descargas):

   # Bibliotecas necesarias
   import os
   import requests

   # Crea la carpeta donde se almacenarán los archivos descargados
   os.makedirs(Carpeta_archivos_descargas, exist_ok=True)

   print ('Empieza el proceso de descargar las bases de datos')

   # Asturias              No Funciona por un problema con el protocolo FTP, descargar desde Firefox
   if CCAA == 0 or CCAA == 3:
      print ('La base de datos de Asturias no se pudo descargar, para descargar la BBDD de Asturias ir a: https://datos.gob.es/es/catalogo/a03002951-eficiencia-energetica-edif-viv, usar Internet Explorer porque da un problema con el protocolo FTP')

   # Aragón                Como hay a veces errores varios al descargar archivos, cambios de servidores y así lo dejo todo con try except y que salte un aviso de la que ha fallado
   if CCAA == 0 or CCAA == 2:
      try:
         # Definimos la URL del archivo a descargar
         remote_url = r'https://opendata.aragon.es/GA_OD_Core/download?view_id=237&formato=xlsx'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + r'\Aragon.xlsx'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
               file.write(data.content)

         print ('BBDD Aragón descargada')
      except:
            print ('BBDD Aragón no se ha podido descargar')
   
   # Baleares
   if CCAA == 0 or CCAA == 4:
      try:
         # Definimos la URL del archivo a descargar
         remote_url = r'https://catalegdades.caib.cat/api/views/bhvx-p8vz/rows.csv?accessType=DOWNLOAD&bom=true&format=true'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + r'\Baleares.csv'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
            file.write(data.content)
         print ('BBDD Baleares descargada')
      except:
            print ('BBDD Baleares no se ha podido descargar')

   # Canarias
   if CCAA == 0 or CCAA == 5:
      try:
         # Definimos la URL del archivo a descargar
         remote_url = r'https://datos.canarias.es/catalogos/general/dataset/ca2b3a6c-241b-4fe1-ba6b-f35257ce9604/resource/7094974b-2642-45bf-a5c7-636692d2b3ec/download/rcee202401.csv'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + r'\Canarias.csv'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
            file.write(data.content)

         print ('BBDD Canarias descargada')
      except:
            print ('BBDD Canarias no se ha podido descargar')

   # Cantabria
   if CCAA == 0 or CCAA == 6:
      try:
         # Definimos la URL del archivo a descargar
         remote_url = r'https://dgicc.cantabria.es//documents/16626/22038372/DATOS_RCEEC-05042022.xlsx/53189aaa-87ac-60a6-c061-7edbef59716a?t=1650285779330'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + r'\Cantabria.xlsx'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
            file.write(data.content)
         print ('BBDD Cantabria descargada')
      except:
            print ('BBDD Cantabria no se ha podido descargar')

   # Cataluña
   if CCAA == 0 or CCAA == 9:
      try:
         # Definimos la URL del archivo a descargar
         remote_url = r'https://analisi.transparenciacatalunya.cat/api/views/j6ii-t3w2/rows.csv?accessType=DOWNLOAD&bom=true&format=true&delimiter=%3B&sorting=true'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + r'\Cataluña.csv'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
            file.write(data.content)

         print ('BBDD Cataluña descargada')
      except:
            print ('BBDD Cataluña no se ha podido descargar')
   
   # Castilla la Mancha
   if CCAA == 0 or CCAA == 8:
      try:
         # Definimos la URL del archivo a descargar
         remote_url = r'https://datosabiertos.castillalamancha.es/node/733/dataset/download'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + r'\CLM.zip'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
            file.write(data.content)
         print ('BBDD Castilla la Mancha descargada')
      except:
            print ('BBDD Castilla la Mancha no se ha podido descargar')

   # Comunidad Valenciana
   if CCAA == 0 or CCAA == 10:
      try:
         # Se descarga cada provincia por separado y cada año por separado porque son archivos diferentes a unir luego, Importante hay que actualizar con la información nueva que salga año a año, saldrá la pestaña del 2023 próximamente, con su propio link
         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2022&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2022.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2022&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2022.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2022&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2022.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2021&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2021.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2021&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2021.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2021&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2021.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2020&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2020.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2020&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2020.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2020&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2020.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2019&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2019.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2019&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2019.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2019&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2019.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2018&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2018.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2018&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2018.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2018&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2018.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2017&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2017.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2017&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2017.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2017&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2017.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2016&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2016.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2016&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2016.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2016&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2016.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2015&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2015.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2015&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2015.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2015&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2015.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2014&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2014.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2014&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2014.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2014&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2014.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2013&provincia=ALICANTE&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Alicante_2013.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2013&provincia=CASTELL%C3%93N&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Castellon_2013.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)

         remote_url = r'https://gceedadesobertes.aven.es/dadesobertes/Home/GetFile?anyo=2013&provincia=VALENCIA&tipo=ETIQUETA&formato=csv'
         local_file = Carpeta_archivos_descargas + r'\CVALENCIANA_Valencia_2013.csv'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
         print ('BBDD Comunidad Valenciana descargada')
      except:
            print ('BBDD Comunidad Valenciana no se ha podido descargar')

   # Castilla y León
   if CCAA == 0 or CCAA == 7:
      try:
         # Definimos la URL del archivo a descargar
         remote_url = r'https://datosabiertos.jcyl.es/web/jcyl/risp/es/energia/certificados-eficiencia/1285094021912.csv'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + r'\CYL.csv'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
            file.write(data.content)
         print ('BBDD Castilla y León descargada')
      except:
            print ('BBDD Castilla y León no se ha podido descargar')
   
   # Galicia               Si funciona el link pero te lleva a un captcha de No soy un robot, hay que hacerlo a mano
   if CCAA == 0 or CCAA == 12:
      print ('La base de datos de Galicia no se pudo descargar, para descargar la BBDD de Galicia ir a: https://datos.gob.es/es/catalogo/a12002994-registro-de-certificados-de-eficiencia-energetica-de-edificios-de-galicia, descargar el csv y resolver el captcha')

 
   """ Hacer_esta_BBDD = 1
   if Hacer_esta_BBDD == 1 or Hacer_todas_las_BBDD == 1 :
         # Definimos la URL del archivo a descargar
         remote_url = 'https://abertos.xunta.gal/catalogo/economia-empresa-emprego/-/dataset/0432/rexistro-certificados-eficiencia-enerxetica/001/acceso-aos-datos.csv'

         # Definimos el nombre del archivo local a guardar
         local_file = Carpeta_archivos_descargas + '\Galicia.csv'

         # Se envía la petición HTTP Get para la obtención del recurso
         data = requests.get(remote_url)

         # Guardamos el archivo de manera local
         with open(local_file, 'wb')as file:
            file.write(data.content)

         print ('BBDD Galicia descargada') """

   # Navarra               A veces no funciona, están los enlaces o caídos o llevan a un csv totalmente roto, ya lo arreglarán, el link al que ir es este: https://datos.gob.es/es/catalogo/a15002917-certificaciones-energeticas
   if CCAA == 0 or CCAA == 15:
      try:
            # Definimos la URL del archivo a descargar
            remote_url = r'https://datosabiertos.navarra.es/dataset/ffaab043-95d7-418e-89bb-8c29abdb797c/resource/0e2e3204-c0e3-418d-87bb-a2949b676f5f/download/resultadocertenerg.csv'
            # Hay varios links con diferentes datos, el mejor es el de arriba por ahora 'https://datosabiertos.navarra.es/api/services/datastore-downloader/0e2e3204-c0e3-418d-87bb-a2949b676f5f.xlsx'

            # Definimos el nombre del archivo local a guardar
            local_file = Carpeta_archivos_descargas + r'\CNavarra.csv'

            # Se envía la petición HTTP Get para la obtención del recurso
            data = requests.get(remote_url)

            # Guardamos el archivo de manera local
            with open(local_file, 'wb')as file:
               file.write(data.content)
            print ('BBDD Navarra descargada')
      except:
            print ('BBDD Navarra no se ha podido descargar')

   # La Rioja
   if CCAA == 0 or CCAA == 17:
      try:
            # Definimos la URL del archivo a descargar
            remote_url = r'https://ias1.larioja.org/opendata/download?r=Y2Q9ODgyfGNmPTAz'

            # Definimos el nombre del archivo local a guardar
            local_file = Carpeta_archivos_descargas + r'\Rioja.csv'

            # Se envía la petición HTTP Get para la obtención del recurso
            data = requests.get(remote_url)

            # Guardamos el archivo de manera local
            with open(local_file, 'wb')as file:
               file.write(data.content)
            print ('BBDD La Rioja descargada')

      except:
            print ('BBDD La Rioja no se ha podido descargar')

   # Andalucía
   if CCAA == 0 or CCAA == 1:
      try:
         # Se descarga cada provincia por separado
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/78e189b6-cd99-4540-93dd-5bd40c94f328/download/almeria.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Almería.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Almería no se ha podido descargar')

      try:
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/863f4a34-8160-4254-982a-99191449c32f/download/cadiz.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Cadiz.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Cádiz no se ha podido descargar')

      try:
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/0171214a-1f02-4c19-913d-7b01303f19b3/download/cordoba.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Cordoba.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Córdoba no se ha podido descargar')

      try:
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/d90129b6-0aa6-4908-a86b-08c934963404/download/granada.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Granada.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Granada no se ha podido descargar')

      try:
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/18e1b0e3-5266-43ce-9266-54c48e6f4ee4/download/huelva.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Huelva.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Huelva no se ha podido descargar')

      try:
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/ed94818f-5a1d-4e5c-b011-a81853648500/download/jaen.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Jaen.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Jaén no se ha podido descargar')

      try:
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/e79cc287-2120-4ee6-8142-f95f2f105118/download/malaga.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Malaga.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Málaga no se ha podido descargar')

      try:
         remote_url = r'https://www.juntadeandalucia.es/datosabiertos/portal/dataset/cb915b9d-f849-421e-99e3-61acec4aaff8/resource/81ca9969-ec79-48ce-ae45-6cbcac4c4181/download/sevilla.7z'
         local_file = Carpeta_archivos_descargas + r'\ANDALUCÍA_Sevilla.7z'
         data = requests.get(remote_url)
         with open(local_file, 'wb')as file:
            file.write(data.content)
      except:
         print ('BBDD ANDALUCÍA_Sevilla no se ha podido descargar')
         
      print ('BBDD Andalucía descargada')


   print ('Terminado (De Asturas y Galicia no se pueden descargar sus BBDD)')
