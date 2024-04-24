 # Proceso de la información:
 #   - E: Catastro alfanumérico (y consulta masiva del catastro): Conversión de formatos y manipulación de datos.

 # Este script controla el paso E: Maneja los Scripts para emplear los datos del catastro alfanumérico y de la descarga masiva de datos

"""  Pasos que controla este script:
   - E_3: Catastro alfanumérico: Lee los archivos .cat y divide el archivo en sus tipos de registro (parcela, unidad constructiva, contrucción y bien inmueble) con su info asociada
   - E_4: Catastro alfanumérico: Con el paso anterior agrupa los resultados de cada parte a escala de edificio tomando la información que nos interesa de cada apartado
   - E_5: Catastro alfanumérico: Con el paso anterior une toda la información en una BBDD a escala edificio para unir con el GIS de edif de toda españa """

 #         Antes de nada debemos elegir qué queremos analizar, para ello hay una lista de decisiones, esta lista controla qué resultados obtendremos

import numpy as np

def Alphanumeric_cadastre (PROV, folder_read_files, Extract_ZIP_files, building_scale_cadastre, building_unit_scale_cadastre, drop_unused_columns, columns_to_use_buildings, columns_to_use_building_units):

    Realizar_proceso_CatastroAlfanumérico = True           # Si quiero realizar el proceso de convertir todas las BBDD del catastro alfanumérico que hayamos descargado en datos por edificio (True o False)

    # Pasos dentro del Proceso del catastro alfanumérico
    Extraer_CAT = Extract_ZIP_files                                   # Si quiero extraer de los zip de la descarga del catastro los CAT para trabajarlos
    Tratar_CAT = building_scale_cadastre                              # Si quiero tratar los CAT para sacar la información por edificio a nivel de provincia
    Unir_por_país = building_scale_cadastre                           # Si quiero combinar la información a escala nacional
    Tratar_CAT_escala_BI = building_unit_scale_cadastre               # Lo mismo que el de Tratar_CAT pero la información la devuelve a escala de bien inmueble y no a escala de edificio
    Unir_por_país_escala_BI = building_unit_scale_cadastre            # Lo mismo que el de Unir_por_país pero la información la devuelve a escala de bien inmueble y no a escala de edificio

    # Decisiones sólo para el catastro alfanumérico. 
    uso_Pandas_o_Polars = 1                                # Hemos implementado el código en pandas (0) y en polars (1). El segundo es mucho más rápido, pero el primero no dará problemas con el separador que hemos tenido que poner en polars ($) y lo hemos testeado más, en general probar la opcion de polars y lo que no salga bien hacerlo en pandas
    Unir_por_país_csv_o_parquet = 0                        # Si queremos unir las provincias por sus archivos en csv (0) o en parquet (1). Parquet es mucho más rápido, pero hay que haber podido guardar todas las provincias en parquet y hay algunos errores que resolver

    # Para ello hay que elegir un valor en la variable CCAA en base al switch_CCAA de debajo:
    # Están todas las CCAA y ciudades autónomas en previsión de que aporten los datos, (Navarra y País Vasco no están en el catastro español)

    switch_PROV = {
        0: 'Todas las provincias disponibles',
        1: 'Araba/Álava',
        2: 'Albacete',
        3: 'Alicante/Alacant',
        4: 'Almería',
        5: 'Ávila',
        6: 'Badajoz',
        7: 'Balears, Illes',
        8: 'Barcelona',
        9: 'Burgos',
        10: 'Cáceres',  
        11: 'Cádiz',
        12: 'Castellón/Castelló',    
        13: 'Ciudad Real',
        14: 'Córdoba',
        15: 'Coruña, A',
        16: 'Cuenca',
        17: 'Girona',
        18: 'Granada',
        19: 'Guadalajara',
        20: 'Gipuzkoa',
        21: 'Huelva',
        22: 'Huesca',
        23: 'Jaén',
        24: 'León',
        25: 'Lleida',
        26: 'Rioja, La',
        27: 'Lugo',
        28: 'Madrid',
        29: 'Málaga',
        30: 'Murcia',
        31: 'Navarra',
        32: 'Ourense',
        33: 'Asturias',
        34: 'Palencia',
        35: 'Palmas, Las',
        36: 'Pontevedra',
        37: 'Salamanca',
        38: 'Santa Cruz de Tenerife',
        39: 'Cantabria',
        40: 'Segovia',
        41: 'Sevilla',
        42: 'Soria',
        43: 'Tarragona',
        44: 'Teruel',
        45: 'Toledo',
        46: 'Valencia/València',
        47: 'Valladolid',
        48: 'Bizkaia',
        49: 'Zamora',
        50: 'Zaragoza',
        51: 'Ceuta',
        52: 'Melilla',
        99: 'Error',
        }
    # El listado sigue el código de Provincias del INE: https://www.ine.es/daco/daco42/codmun/cod_provincia.htm (y añado la 0 Y LA 99 (Error))


    #                                  A continuación se detallan todos los pasos, la elección de si se hacen o no está en lista_decisiones, pero aquí hay cuestiones como las rutas por defecto

    #      Catastro alfanumérico
    # Paso 1, Descargar del catastro alfanumérico los datos a tratar, este paso se hace a mano hasta que no haya una API del catastro a la que acudir
    # En esta carpeta meter solo los archivos .cat
    Carpeta_archivos_descargas_CA = folder_read_files  # La carpeta donde tenemos las BBDD del catastro alfanumérico

    # Paso 2, Provincia a provincia hará los pasos indicados y finalmente los unirá todos los archivos por edificio en uno solo, creo que es lo más rápido en términos de tiempo

    Carpeta_archivos_guardar = folder_read_files + r'\Datos del Catastro alfanumerico por edificio'         # La carpeta donde se guardarán los nuevos archivos

    # Paso 3, Para cada provincia lee los datos del .cat, los separa por tipo de registro que nos interesa y los guarda en un archivo independiente para cada tipo de registro

    # Paso 4, Agrupa los datos de cada tipo de registro por edificio

    # Paso 5, Agrupa los datos de cada tipo de registro por edificio en nuna sola BBDD con toda la info disponible por edificio

    # Paso 6, Agrupa los datos del paso 5 de las diferentes provincias

    # A partir de este punto se ejecuta el código paso a paso (No tocar)

    print ('Empieza el paso E con ' + str(switch_PROV.get(PROV)))
    import os
    import pandas as pd
    import polars as pl
    from time import time

    # Para conocer cuánto tarda el proceso
    inicio  = time()


    # Catastro Alfanumérico
    if Realizar_proceso_CatastroAlfanumérico == True:
        print ('Empieza el paso E - Catastro Alfanumérico')

        if Extraer_CAT == True:
            print ('Empieza el paso E - Extraer la info de los Zip del Catastro')

            from Internal_scripts.Archivoscatastroalfanumerico_y_descargamasiva import E_2_Extrae_y_ordena_zip_catastro
            E_2_Extrae_y_ordena_zip_catastro.Extraer_CAT (Carpeta_archivos_descargas_CA)
        

        if Tratar_CAT == True:
            print ('Empieza el paso E - Tratar la info de los .CAT')
            from Internal_scripts.Archivoscatastroalfanumerico_y_descargamasiva import E_3_Modifica_formato_CAT_Pandas, E_3_Modifica_formato_CAT_Polars, E_4_Agrupa_datos_escala_edificio_Pandas, E_4_Agrupa_datos_escala_edificio_Polars

            os.makedirs(Carpeta_archivos_guardar + '\\' + 'Datos por Provincia', exist_ok=True)          # Crea la carpeta donde guardaremos los datos tratados
            GranBBDD = pd.DataFrame()

            with os.scandir(Carpeta_archivos_descargas_CA + '\\' + 'Archivos_descomprimidos') as carpetas: # Escanea la carpeta donde estarán los archivos descargados y los lee para tratar los .CAT
                for carpeta in carpetas:
                    cprov = 0
                    GranBBDD = pd.DataFrame()
                    n_datos = 0                                           # Las siguientes variables con darán el nº de elementos de cada tipo en el catastro alfanumerico
                    n_F = 0
                    n_UC = 0
                    n_C = 0
                    n_BI= 0
                    try: cprov = int(carpeta.name[:2])                    # Saca el número de provincia que son los dos primeros dígutos del nombre del archivo, es un try except para eliminar errores si hay archivos que no son las carpetas con los .cat
                    except: pass
                    if (PROV == 0 or cprov == PROV):                      # Este if nos permite trabajar según hayamos indicado en la variable PROV
                        print ('Empieza la Provincia de ' + switch_PROV.get(int(carpeta.name[:2])))
                        inicio_prov  = time()
                        with os.scandir(carpeta) as ficheros:             # Escanea la carpeta donde estarán los archivos descargados y los lee para tratar los .CAT
                            for fichero in ficheros:
                                if uso_Pandas_o_Polars == 0:
                                    finca, unidadconstructiva, construccion, inmueble, a, b, c, d, e = E_3_Modifica_formato_CAT_Pandas.TratarCAT (fichero, Carpeta_archivos_guardar)
                                    edificios_Completos = E_4_Agrupa_datos_escala_edificio_Pandas.AgruparCATporEdificio (finca, unidadconstructiva, construccion, inmueble, Carpeta_archivos_guardar, fichero.name)
                                else:
                                    finca, unidadconstructiva, construccion, inmueble, a, b, c, d, e = E_3_Modifica_formato_CAT_Polars.TratarCAT (Carpeta_archivos_descargas_CA, carpeta, fichero, Carpeta_archivos_guardar)
                                    edificios_Completos = E_4_Agrupa_datos_escala_edificio_Polars.AgruparCATporEdificio (finca, unidadconstructiva, construccion, inmueble, Carpeta_archivos_guardar, fichero.name)                     
                                    n_datos = n_datos + a
                                    n_F = n_F + b
                                    n_UC = n_UC + c
                                    n_C = n_C + d
                                    n_BI = n_BI + e
                                    GranBBDD = pd.concat([GranBBDD, edificios_Completos], axis=0)
                        #GranBBDD.to_parquet(Carpeta_archivos_guardar + '\\' + 'Datos por Provincia' + '\\' + carpeta.name + ".gzip", compression='gzip', index=False)
                        GranBBDD.to_csv(Carpeta_archivos_guardar + '\\' + 'Datos por Provincia' + '\\' + carpeta.name + ".csv", encoding='utf-8', index=False)
                        
                        duracion_prov = time() - inicio
                        with open(Carpeta_archivos_guardar + '\\' + r"Datos_archivo_cat_" + carpeta.name + ".txt", 'w') as f:
                                            f.write('En la provincia ' + switch_PROV.get(int(carpeta.name[:2])) + ' con código ' + carpeta.name + '\nEn total hay: ' + str(n_datos) + ' datos \nFincas: ' + str (n_F) + '\nUnidades Constructivas: ' + str(n_UC) + '\nConstrucciones: ' + str(n_C) + '\nBienes inmuebles: ' + str(n_BI) + '\nY ha tardado: ' + str(duracion_prov) + ' segundos' )

            print ('Terminado el paso E - Tratar los CAT')

        # Si quiero combinar la información a escala nacional
        if Unir_por_país == True:
            inicio_prov  = time()
            GranBBDD = pd.DataFrame()     # Aquí polars me da errores por unir int y float, para alternar entre pandas y polars hay que cambiar pd por pl en esta linea y la 231 y 232 y en la 233 el to_csv por write_csv
            carpeta_provincias = Carpeta_archivos_guardar + '\\' + 'Datos por Provincia'
            dtype_dict = {'Provincia': str, 'CMunicipioINE': str, 'CMunicipioDGC': str, 'Tipologia_constructiva': str}   # Hay columnas como el código de provincia o de municipio que son números y se leen como int pero deberían ser strings
            if Unir_por_país_csv_o_parquet == 1:
                with os.scandir(carpeta_provincias) as ficheros:                # Escanea la carpeta donde estarán los archivos de los datos por edificio a escala de provincia
                    for fichero in ficheros:
                        df = (pd.read_csv(fichero, dtype=dtype_dict))
                        GranBBDD = pd.concat([GranBBDD, df], axis=0)
                
                # Sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino los errores catastrales
                pre_borrar = GranBBDD.shape[0]
                GranBBDD = GranBBDD.drop_duplicates(subset=['ReferenciaCatastral_parcela'], keep=False)
                duplicados = GranBBDD.shape[0] - pre_borrar
                if duplicados != 0:
                    print ('Se han borrado por duplicados ' + str(duplicados) + ' edificios')

                # Para guardar en formato parquet hay que definir el tipo de algunas columnas que sino dan error
                GranBBDD['Tipologia_constructiva'] = GranBBDD['Tipologia_constructiva'].astype(str)
                GranBBDD.to_parquet(Carpeta_archivos_guardar + r"\Edificios_España_Completos" + ".gzip", compression='gzip', index=False)
            else:
                with os.scandir(carpeta_provincias) as ficheros:                # Escanea la carpeta donde estarán los archivos de los datos por edificio a escala de provincia
                    for fichero in ficheros:
                        print(fichero)
                        df = (pd.read_csv(carpeta_provincias + '\\' + fichero.name, dtype=dtype_dict))
                        GranBBDD = pd.concat([GranBBDD, df])
                
                # Sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino los errores catastrales
                pre_borrar = GranBBDD.shape[0]
                GranBBDD = GranBBDD.drop_duplicates(subset=['ReferenciaCatastral_parcela'], keep=False)
                duplicados = GranBBDD.shape[0] - pre_borrar
                if duplicados != 0:
                    print ('Se han borrado por duplicados ' + str(duplicados) + ' edificios')
                
                # Para guardar en formato parquet hay que definir el tipo de algunas columnas que sino dan error
                GranBBDD['Tipologia_constructiva'] = GranBBDD['Tipologia_constructiva'].astype(str)
                GranBBDD.to_parquet(Carpeta_archivos_guardar + r"\Edificios_España_Completos" + ".gzip", compression='gzip', index=False)
                GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Edificios_España_Completos" + ".csv")

            if drop_unused_columns == True:
                GranBBDD = GranBBDD[GranBBDD.columns.intersection(columns_to_use_buildings)]

                # Elimino todos los edificios que son parcelas sin edificar (lo hago por Sup_elementos_urbanos == 0, es la superficie de los bienes inmuebles sumada)
                GranBBDD.insert(1, 'Sup_total', GranBBDD['S_Viv'] + GranBBDD['S_Almacen'] + GranBBDD['S_Ind'] + GranBBDD['S_Of'] + GranBBDD['S_Com']
                        + GranBBDD['S_Dep'] + GranBBDD['S_Esp'] + GranBBDD['S_Host'] + GranBBDD['S_San'] + GranBBDD['S_Cult'] + GranBBDD['S_Rel'] + GranBBDD['S_Sin'] + GranBBDD['S_IAg'] + GranBBDD['S_Ag']
                        )
                GranBBDD['Sup_total'] = GranBBDD['Sup_total']. fillna('None')
                GranBBDD['Coincide'] = np.where((GranBBDD['Sup_total']!= 'None'), 'Si','Bien')
                GranBBDD = GranBBDD.loc[(GranBBDD['Coincide'] == 'Si')]
                GranBBDD = GranBBDD.drop(['Coincide'], axis=1)
                GranBBDD = GranBBDD.loc[GranBBDD.loc[:, 'Sup_total'] != 0]
                GranBBDD = GranBBDD.drop(['Sup_total'], axis=1)

                # Doy el uso principal del edificio, en base a la superficie del uso más grande de los bienes inmuebles del edificio
                sup = GranBBDD.loc[:,['S_Viv', 'S_Almacen', 'S_Ind', 'S_Of', 'S_Com', 'S_Dep', 'S_Esp', 'S_Host', 'S_San', 'S_Cult', 'S_Rel', 'S_Sin', 'S_IAg', 'S_Ag']]
                ind = np.argsort(-sup.values, axis=1)
                uso_p = ind[:, 0]
                GranBBDD['Uso_principal'] = pd.Series(uso_p).replace({0: 'Residencial', 1: 'Almacén-Estacionamiento', 2: 'Industrial', 
                                                                      3: 'Oficinas', 4: 'Comercial', 5: 'Deportivo', 6: 'Espectáculos', 
                                                                      7: 'Ocio y Hostelería', 8: 'Sanidad y Beneficencia', 9: 'Cultural', 
                                                                      10: 'Religioso', 11: 'Edificio singular', 12: 'Industrial agrario', 
                                                                      13: 'Agrario'
                                                                    })

                # print (df.columns)
                GranBBDD.to_parquet(Carpeta_archivos_guardar + r"\Edificios_España_Completos" + "_Reducido" + ".gzip", compression='gzip', index=False)
                GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Edificios_España_Completos" + "_Reducido" + ".csv")




            print (GranBBDD.dtypes)
            n_edif = GranBBDD.shape[0]
            duracion_prov = time() - inicio
            with open(Carpeta_archivos_guardar + '\\' + r"Duración_proceso_Unir_escala_nacional" + ".txt", 'w') as f:
                        f.write('Unir los datos a escala país ha costado: ' + str(duracion_prov) + ' segundos' 
                                + '\nEdificios en el archivo resultante de unir toda España hay (ya quitados los duplicados): ' + str(n_edif)
                                + '\nEdificios que se han eliminado por estar duplicados (se eliminan todos los duplicados): ' + str(duplicados)
                                )

                    # Versión Pandas
        # Si quiero combinar la información a escala nacional
        # if Unir_por_país == True:
        #     inicio_prov  = time()
        #     GranBBDD = pd.DataFrame()
        #     carpeta_provincias = Carpeta_archivos_guardar + '\\' + 'Datos por Provincia'
        #     if Unir_por_país_csv_o_parquet == 1:
        #         with os.scandir(carpeta_provincias) as ficheros:                # Escanea la carpeta donde estarán los archivos de los datos por edificio a escala de provincia
        #             for fichero in ficheros:
        #                 df = (pd.read_parquet(fichero))
        #                 GranBBDD = pd.concat([GranBBDD, df], axis=0)
        #         GranBBDD.to_parquet(carpeta_provincias + r"\Edificios_España_Completos" + ".gzip", compression='gzip', index=False)
        #     else:
        #         with os.scandir(carpeta_provincias) as ficheros:                # Escanea la carpeta donde estarán los archivos de los datos por edificio a escala de provincia
        #             for fichero in ficheros:
        #                 df = (pd.read_csv(fichero))
        #                 GranBBDD = pd.concat([GranBBDD, df], axis=0)
        #         GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Edificios_España_Completos" + ".csv", encoding='utf-8', index=False)
        #     print (GranBBDD.dtypes)
        #     duracion_prov = time() - inicio
        #     with open(Carpeta_archivos_guardar + '\\' + r"Duración_proceso_Unir_escala_nacional_" + carpeta.name + ".txt", 'w') as f:
        #                 f.write('Unir los datos a escala país ha costado: ' + str(duracion_prov) + ' segundos' )


        if Tratar_CAT_escala_BI == True:
            print ('Empieza el paso E - Tratar la info de los .CAT resultado a escala BI')
            from Internal_scripts.Archivoscatastroalfanumerico_y_descargamasiva import E_3_1_Escala_BI_Modifica_formato_CAT_Polars, E_4_2_Agrupa_datos_escala_edificio_Polars

            os.makedirs(Carpeta_archivos_guardar + '\\' + 'Datos por Provincia_escala_BI', exist_ok=True)          # Crea la carpeta donde guardaremos los datos tratados
            GranBBDD = pd.DataFrame()

            with os.scandir(Carpeta_archivos_descargas_CA + '\\' + 'Archivos_descomprimidos') as carpetas: # Escanea la carpeta donde estarán los archivos descargados y los lee para tratar los .CAT
                for carpeta in carpetas:
                    cprov = 0
                    GranBBDD = pd.DataFrame()
                    n_datos = 0                                           # Las siguientes variables con darán el nº de elementos de cada tipo en el catastro alfanumerico
                    n_F = 0
                    n_UC = 0
                    n_C = 0
                    n_BI= 0
                    try: cprov = int(carpeta.name[:2])                    # Saca el número de provincia que son los dos primeros dígutos del nombre del archivo, es un try except para eliminar errores si hay archivos que no son las carpetas con los .cat
                    except: pass
                    if (PROV == 0 or cprov == PROV):                      # Este if nos permite trabajar según hayamos indicado en la variable PROV
                        print ('Empieza la Provincia de ' + switch_PROV.get(int(carpeta.name[:2])))
                        inicio_prov  = time()
                        with os.scandir(carpeta) as ficheros:             # Escanea la carpeta donde estarán los archivos descargados y los lee para tratar los .CAT
                            for fichero in ficheros:
                                construccion, inmueble, a, d, e = E_3_1_Escala_BI_Modifica_formato_CAT_Polars.TratarCAT (Carpeta_archivos_descargas_CA, carpeta, fichero, Carpeta_archivos_guardar)
                                edificios_Completos = E_4_2_Agrupa_datos_escala_edificio_Polars.AgruparCATporEdificio (construccion, inmueble, Carpeta_archivos_guardar, fichero.name)                     
                                n_datos = n_datos + a
                                n_C = n_C + d
                                n_BI = n_BI + e
                                GranBBDD = pd.concat([GranBBDD, edificios_Completos], axis=0)
                        #GranBBDD.to_parquet(Carpeta_archivos_guardar + '\\' + 'Datos por Provincia' + '\\' + carpeta.name + ".gzip", compression='gzip', index=False)
                        GranBBDD.to_csv(Carpeta_archivos_guardar + '\\' + 'Datos por Provincia_escala_BI' + '\\' + carpeta.name + ".csv", encoding='utf-8', index=False)
                        
                        duracion_prov = time() - inicio
                        with open(Carpeta_archivos_guardar + '\\' + r"Datos_archivo_cat_" + carpeta.name + ".txt", 'w') as f:
                                            f.write('En la provincia ' + switch_PROV.get(int(carpeta.name[:2])) + ' con código ' + carpeta.name + '\nEn total hay: ' + str(n_datos) + ' datos \nConstrucciones: ' + str(n_C) + '\nBienes inmuebles: ' + str(n_BI) + '\nY ha tardado: ' + str(duracion_prov) + ' segundos' )

            print ('Terminado el paso E - Tratar los CAT resultado a escala BI')

        # Si quiero combinar la información a escala nacional
        if Unir_por_país_escala_BI == True:
            inicio_prov  = time()
            GranBBDD = pd.DataFrame()     # Aquí polars me da errores por unir int y float, para alternar entre pandas y polars hay que cambiar pd por pl en esta linea y la 231 y 232 y en la 233 el to_csv por write_csv
            carpeta_provincias = Carpeta_archivos_guardar + '\\' + 'Datos por Provincia_escala_BI'
            dtype_dict = {'Provincia': str, 'CMunicipioINE_BI': str, 'CMunicipioDGC': str, 'Tipologia_constructiva': str}
            if Unir_por_país_csv_o_parquet == 1:
                with os.scandir(carpeta_provincias) as ficheros:                # Escanea la carpeta donde estarán los archivos de los datos por edificio a escala de provincia
                    for fichero in ficheros:
                        df = (pd.read_csv(fichero, dtype=dtype_dict))
                        GranBBDD = pd.concat([GranBBDD, df], axis=0)
                
                # Sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino los errores catastrales
                pre_borrar = GranBBDD.shape[0]
                GranBBDD = GranBBDD.drop_duplicates(subset=['Referencia_BI'], keep=False)
                duplicados = GranBBDD.shape[0] - pre_borrar
                if duplicados != 0:
                    print ('Se han borrado por duplicados ' + str(duplicados) + ' Bienes inmuebles')

                # Para guardar en formato parquet hay que definir el tipo de algunas columnas que sino dan error
                GranBBDD['Tipologia_constructiva'] = GranBBDD['Tipologia_constructiva'].astype(str)

                GranBBDD.to_parquet(Carpeta_archivos_guardar + r"\Edificios_España_Completos_escala_BI" + ".gzip", compression='gzip', index=False)
            else:
                with os.scandir(carpeta_provincias) as ficheros:                # Escanea la carpeta donde estarán los archivos de los datos por edificio a escala de provincia
                    for fichero in ficheros:
                        print(fichero)
                        df = (pd.read_csv(carpeta_provincias + '\\' + fichero.name, dtype=dtype_dict))
                        GranBBDD = pd.concat([GranBBDD, df])
                
                # Sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino los errores catastrales
                pre_borrar = GranBBDD.shape[0]
                GranBBDD = GranBBDD.drop_duplicates(subset=['Referencia_BI'], keep=False)
                duplicados = GranBBDD.shape[0] - pre_borrar
                if duplicados != 0:
                    print ('Se han borrado por duplicados ' + str(duplicados) + ' Bienes inmuebles')

                # Para guardar en formato parquet hay que definir el tipo de algunas columnas que sino dan error
                GranBBDD['Tipologia_constructiva'] = GranBBDD['Tipologia_constructiva'].astype(str)
                GranBBDD.to_parquet(Carpeta_archivos_guardar + r"\Edificios_España_Completos_escala_BI" + ".gzip", compression='gzip', index=False)
                GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Edificios_España_Completos_escala_BI" + ".csv")

            if drop_unused_columns == True:
                GranBBDD = GranBBDD[GranBBDD.columns.intersection(columns_to_use_building_units)]

                # Elimino todos los edificios que son parcelas sin edificar (lo hago por Sup_elementos_urbanos == 0, es la superficie de los bienes inmuebles sumada)
                GranBBDD.insert(1, 'Sup_total', GranBBDD['S_Viv'] + GranBBDD['S_Almacen'] + GranBBDD['S_Ind'] + GranBBDD['S_Of'] + GranBBDD['S_Com']
                        + GranBBDD['S_Dep'] + GranBBDD['S_Esp'] + GranBBDD['S_Host'] + GranBBDD['S_San'] + GranBBDD['S_Cult'] + GranBBDD['S_Rel'] + GranBBDD['S_Sin'] + GranBBDD['S_IAg'] + GranBBDD['S_Ag']
                        )
                GranBBDD['Sup_total'] = GranBBDD['Sup_total']. fillna('None')
                GranBBDD['Coincide'] = np.where((GranBBDD['Sup_total']!= 'None'), 'Si','Bien')
                GranBBDD = GranBBDD.loc[(GranBBDD['Coincide'] == 'Si')]
                GranBBDD = GranBBDD.drop(['Coincide'], axis=1)
                GranBBDD = GranBBDD.loc[GranBBDD.loc[:, 'Sup_total'] != 0]
                GranBBDD = GranBBDD.drop(['Sup_total'], axis=1)

                # Doy el uso principal del edificio, en base a la superficie del uso más grande de los bienes inmuebles del edificio
                sup = GranBBDD.loc[:,['S_Viv', 'S_Almacen', 'S_Ind', 'S_Of', 'S_Com', 'S_Dep', 'S_Esp', 'S_Host', 'S_San', 'S_Cult', 'S_Rel', 'S_Sin', 'S_IAg', 'S_Ag']]
                ind = np.argsort(-sup.values, axis=1)
                uso_p = ind[:, 0]
                GranBBDD['Uso_principal'] = pd.Series(uso_p).replace({0: 'Residencial', 1: 'Almacén-Estacionamiento', 2: 'Industrial', 
                                                                      3: 'Oficinas', 4: 'Comercial', 5: 'Deportivo', 6: 'Espectáculos', 
                                                                      7: 'Ocio y Hostelería', 8: 'Sanidad y Beneficencia', 9: 'Cultural', 
                                                                      10: 'Religioso', 11: 'Edificio singular', 12: 'Industrial agrario', 
                                                                      13: 'Agrario'
                                                                    })

                # print (df.columns)
                GranBBDD.to_parquet(Carpeta_archivos_guardar + r"\Edificios_España_Completos_escala_BI" + "_Reducido" + ".gzip", compression='gzip', index=False)
                GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Edificios_España_Completos_escala_BI" + "_Reducido" + ".csv")


            print (GranBBDD.dtypes)
            n_edif = GranBBDD.shape[0]
            duracion_prov = time() - inicio
            with open(Carpeta_archivos_guardar + '\\' + r"Duración_proceso_Unir_escala_nacional_BI" + ".txt", 'w') as f:
                        f.write('Unir los datos a escala país ha costado: ' + str(duracion_prov) + ' segundos' + 
                                '\nBienes inmuebles en el archivo resultante de unir toda España hay (ya quitando duplicados): ' + str(n_edif)
                                + '\nBienes inmuebles que se han eliminado por estar duplicados (se eliminan todos los duplicados): ' + str(duplicados)
                                )

            print ('Terminado el paso E - Tratar los CAT')

    # Para conocer cuánto tarda el proceso
    duracion = (time() - inicio)/60
    with open(Carpeta_archivos_guardar + '\\' + r"Duración_proceso_E_Script_clave" + ".txt", 'w') as f:
                    f.write('Realizar todo el proceso E_Script_clave ha tardado ' + str(duracion) + ' minutos' )

    print ('Terminado todo el paso E')


