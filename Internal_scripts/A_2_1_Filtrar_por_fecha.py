 # Para el artículo se necesitan los datos a fecha 1/1/2020, para ello eliminamos los certificados posteriores
def Filtrar_fecha (CCAA, Fecha_filtro, Carpeta_archivos_leer):

    # Bibliotecas necesarias
    import os
    import pandas as pd
    import numpy as np
    import xlrd 
    print ('Empieza a separar por anteriores o iguales a ' + str(Fecha_filtro) + ' y posteriores')

    # Crea la carpeta donde se almacenarán los archivos modificados
    os.makedirs('Separados_por_fecha', exist_ok=True)
    os.makedirs('Separados_por_fecha\BBDD_Anteriores_a_1_1_' + str(Fecha_filtro + 1), exist_ok=True)
    os.makedirs('Separados_por_fecha\Posteriores_a_1_1_' + str(Fecha_filtro + 1), exist_ok=True)
    os.makedirs('Separados_por_fecha\Errores_en_la_fecha_' + str(Fecha_filtro + 1), exist_ok=True)

    # Crea el informe de número de errores encontrados
    informeBBDD = pd.DataFrame(columns=('Archivo', 'Total de certificados', 'Total de certificados anteriores al 1/1/' + str(Fecha_filtro + 1), 'Total de certificados posteriores al 1/1/' + str(Fecha_filtro + 1), 'Total de certificados con errores en la fecha'))

    # Abajo está el script que usa la función Separar e itera por todos los archivos de la carpeta BBDD_Modificadas
        
    # La función que se va iterando para separar los archivos por fecha

    def Separar(nombre_carpeta, nombre, extensión, Fecha_filtro):
        # Separa los archivos en anterior y posterior al 1/1/2020 (o fecha escogida)
        archivo = nombre_carpeta + '\\' + nombre + '.' + extensión

        if extensión == 'xlsx': # Si es un archivo de excel lo abrirá así y lo guardará luego igual
            df = (pd.read_excel(archivo, skiprows=0))
        else:                   # Así lo abrirá como csv
            df = (pd.read_csv(archivo, skiprows=0))

        Size_original = df.shape[0]

        first_column = df.pop('Fecha_registro')
        first_column = pd.to_numeric(first_column, errors='coerce')
        df.insert(39, 'Fecha_registro', first_column)
        df ['Fecha_registro'] = df ['Fecha_registro'].fillna('None')
        fallos = df.loc[df.loc[:, 'Fecha_registro'] == 'None']
        df = df.loc[df.loc[:, 'Fecha_registro'] != 'None']
        fallos2 = df.loc[df.loc[:, 'Fecha_registro'] < 2013]
        df = df.loc[df.loc[:, 'Fecha_registro'] >= 2013]        
        Post_2020= df.loc[df.loc[:, 'Fecha_registro'] > Fecha_filtro]
        df = df.loc[df.loc[:, 'Fecha_registro'] <= Fecha_filtro]
        fallos = pd.concat([fallos, fallos2], axis=0)
        Size_prev_2020 = df.shape[0]
        Size_post_2020 = Post_2020.shape[0]
        Size_fallos = fallos.shape[0]

        if extensión == 'xlsx': # Si es un archivo de excel lo abrirá así y lo guardará luego igual
            df.to_excel('Separados_por_fecha\BBDD_Anteriores_a_1_1_' + str(Fecha_filtro + 1) + '\\' + nombre + '.' + extensión, index=False)
            Post_2020.to_excel('Separados_por_fecha\Posteriores_a_1_1_' + str(Fecha_filtro + 1) + '\\' + nombre + '.' + extensión, index=False)
            fallos.to_excel('Separados_por_fecha\Errores_en_la_fecha_' + str(Fecha_filtro + 1) + '\\' + nombre + '.' + extensión, index=False)
        else:                   # Así lo guardará como csv
            df.to_csv('Separados_por_fecha\BBDD_Anteriores_a_1_1_' + str(Fecha_filtro + 1) + '\\' + nombre + '.' + extensión, index=False)
            Post_2020.to_csv('Separados_por_fecha\Posteriores_a_1_1_' + str(Fecha_filtro + 1) + '\\' + nombre + '.' + extensión, index=False)
            fallos.to_csv('Separados_por_fecha\Errores_en_la_fecha_' + str(Fecha_filtro + 1) + '\\' + nombre + '.' + extensión, index=False)

        informe = pd.DataFrame({'Archivo':[nombre], 'Total de certificados':[Size_original],'Total de certificados anteriores al 1/1/' + str(Fecha_filtro + 1):[Size_prev_2020], 'Total de certificados posteriores al 1/1/' + str(Fecha_filtro + 1):[Size_post_2020], 'Total de certificados con errores en la fecha':[Size_fallos]})
        return informe

    # Para que coja una CCAA en concreto o todas está este switch
    switch_CCAA = {
        0: 'Todas las CCAA disponibles',
        1: 'MOD_ANDALUCÍA_Almería.xlsx,MOD_ANDALUCÍA_Cádiz.xlsx,MOD_ANDALUCÍA_Córdoba.xlsx,MOD_ANDALUCÍA_Granada.xlsx,MOD_ANDALUCÍA_Huelva.xlsx,MOD_ANDALUCÍA_Jaén.xlsx,MOD_ANDALUCÍA_Malaga.xlsx,MOD_ANDALUCÍA_Sevilla.xlsx',
        2: 'MOD_ARAGÓN.xlsx',
        3: 'MOD_ASTURIAS.xlsx',
        4: 'MOD_BALEARES.xlsx',
        5: 'MOD_CANARIAS.xlsx',
        6: 'MOD_CANTABRIA.xlsx',
        7: 'MOD_CYL.xlsx',
        8: 'MOD_CLM_Albacete.xlsx,MOD_CLM_CiudadReal.xlsx,MOD_CLM_Cuenca.xlsx,MOD_CLM_Guadalajara.xlsx,MOD_CLM_Toledo.xlsx',
        9: 'MOD_CATALUÑA.csv',
        10: 'MOD_CVALENCIANA_Alicante.xlsx,MOD_CVALENCIANA_Castellón.xlsx,MOD_CVALENCIANA_Valencia.xlsx',  
        11: 'Extremadura',
        12: 'MOD_GALICIA.xlsx',   
        13: 'Madrid',
        14: 'Murcia',
        15: 'MOD_NAVARRA.xlsx',
        16: 'País Vasco',
        17: 'MOD_RIOJA.xlsx',
        18: 'Ceuta',
        19: 'Melilla', 
        }

    if CCAA == 0:
    # Lista de archivos a iterar, coge todos los archivos de la carpeta BBDD_Modificadas

        nombre_carpeta = Carpeta_archivos_leer
        ficheros = os.listdir(nombre_carpeta)
        for fichero in ficheros:
            #print (fichero)
            sepcol = fichero.split('.')     # Como fichero contiene el nombre del archivo y la extensión, y luego necesito distinguir entre archivos de excel y csv, lo que hago es dividir el nombre por el punto
            nombre = sepcol[0]              # En esta variable cojo el nombre del archivo
            extensión = sepcol[1]           # En esta variable cojo la extensión del archivo (sin el punto)
            if nombre == 'informe_CCAA' or nombre == 'Tiempos_A_Script_clave':
                pass
            else:
                informe = Separar(nombre_carpeta, nombre, extensión, Fecha_filtro)
                informeBBDD = pd.concat([informeBBDD, informe], axis=0)
                print (nombre + ' separado por fecha')

    else:
    # Coge del swith el nombre del archivo de la CCAA que queremos
    
        nombre_carpeta = Carpeta_archivos_leer
        ficheros = switch_CCAA.get(CCAA)
        ficheros = ficheros.split(',')
        for fichero in ficheros:
            #print (fichero)
            sepcol = fichero.split('.')     # Como fichero contiene el nombre del archivo y la extensión, y luego necesito distinguir entre archivos de excel y csv, lo que hago es dividir el nombre por el punto
            nombre = sepcol[0]              # En esta variable cojo el nombre del archivo
            extensión = sepcol[1]           # En esta variable cojo la extensión del archivo (sin el punto)
            informe = Separar(nombre_carpeta, nombre, extensión, Fecha_filtro)
            informeBBDD = pd.concat([informeBBDD, informe], axis=0)
            print (nombre + ' separado por fecha')

    informeBBDD.to_excel('Separados_por_fecha\Errores_en_la_fecha_' + str(Fecha_filtro + 1) + '\\' + 'InformeErroresFecha_BBDD.xlsx', index=False)
