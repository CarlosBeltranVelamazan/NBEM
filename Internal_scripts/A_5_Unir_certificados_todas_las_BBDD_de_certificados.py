# Uno por Referencia catastral los certificados, pongo el nº de certificados de cada CP, su consumo y emisiones medio y mediano y el nº de certificados por letra
# Navarra y País Vasco no están en el catastro con lo que no se pueden unir por Referencia Catastral

def Unir_BBDD (CCAA, Carpeta_archivos_leer, Carpeta_archivos_guardar, Certificados_uso, Fecha_dato, CEE_unidos_por_edificio):

        import os
        import pandas as pd
        import numpy as np
        import xlrd 
        print ("Empieza el proceso de unir los certificados en una sola super base de datos a nivel nacional") 

        GranBBDD = pd.DataFrame()

        # Importante: BBDD de certificados a unir en una sola. ya vienen unidos en edificios por Referencia Catastral. Usar esta variable para escoger si se emplean todos los certificados, sólo los de uso residencial o sólo los de uso terciario. Esta variable define la ruta de entrada de los archivos. Es necesario haber hecho el correspondiente paso en el script de Eliminar datos incorrectos
        # Importante: En la variable TipoEdificio si pones 0 utiliza todos los certificados, si pones 1 utiliza sólo los de uso residencial, si pones 2 utiliza sólo los de uso terciario
        TipoEdificio = Certificados_uso
        print ("Nota: Navarra y País Vasco no están en el catastro con lo que no se pueden unir por referencia catastral")
        os.makedirs('BBDD_Unidas por Referencia Catastral', exist_ok=True)

        switch_BBDD = {
                0: Carpeta_archivos_leer,
                1: Carpeta_archivos_leer,
                2: Carpeta_archivos_leer}

        # Esto era la idea de quitar las casillas extra para dejar sólo la tabla homogénea, lo he pasado al script A_1 para aligerar los archivos
        #if Quitar_extras == True and CEE_unidos_por_edificio == 0:
          #      quitar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
          #      quitar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
        #else:
        quitar = None

        # Importante: Para que Canarias y Cantabria que no filtran por residencial y terciario estuvieran del tirón lo he filtrado así, con un 1 se suman sus certificados aunque sean todos y no sólo residenciales o terciarios
        Arreglo = 0                                                  # No se recomienda ponerlo en 1, mezcla temas diversos y no aporta mucho
        Carpeta_arreglo = 'BBDD_Unidas por Referencia Catastral\Todos los certificados_' + Fecha_dato

        # Asturias
        if CCAA == 0 or CCAA == 3:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ASTURIAS.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Asturias unida')
                
        # Aragón
        if CCAA == 0 or CCAA == 2:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ARAGÓN.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Aragón unida')

        # Baleares
        if CCAA == 0 or CCAA == 4:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_BALEARES.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Baleares unida')

        # Canarias
        if CCAA == 0 or CCAA == 5:
                if TipoEdificio == 0:
                        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CANARIAS.xlsx'
                        df = (pd.read_excel(archivo, usecols= quitar))
                        GranBBDD = pd.concat([GranBBDD, df], axis=0)
                        print ('BBDD Canarias unida')
                elif TipoEdificio != 0 and Arreglo == 1:
                        archivo = Carpeta_arreglo + '\MOD_CANARIAS.xlsx'
                        df = (pd.read_excel(archivo, usecols= quitar))
                        GranBBDD = pd.concat([GranBBDD, df], axis=0)
                        print ('BBDD Canarias unida')

        # Cantabria
        if CCAA == 0 or CCAA == 6:
                if TipoEdificio == 0:
                        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CANTABRIA.xlsx'
                        df = (pd.read_excel(archivo, usecols= quitar))
                        GranBBDD = pd.concat([GranBBDD, df], axis=0)
                        print ('BBDD Cantabria unida')
                elif TipoEdificio != 0 and Arreglo == 1:
                        archivo = Carpeta_arreglo + '\MOD_CANTABRIA.xlsx'
                        df = (pd.read_excel(archivo, usecols= quitar))
                        GranBBDD = pd.concat([GranBBDD, df], axis=0)
                        print ('BBDD Cantabria unida')

        # Castilla Y León
        if CCAA == 0 or CCAA == 7:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CYL.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Castilla y León unida')

        # Castilla La Mancha
        if CCAA == 0 or CCAA == 8:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Toledo.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Castilla La Mancha (Toledo) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Guadalajara.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Castilla La Mancha (Guadalajara) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Cuenca.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Castilla La Mancha (Cuenca) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_CiudadReal.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Castilla La Mancha (Ciudad Real) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Albacete.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Castilla La Mancha (Albacete) unida')

        # Cataluña
        if CCAA == 0 or CCAA == 9:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CATALUÑA.csv'
                df = (pd.read_csv(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Cataluña unida')

        # Comunidad Valenciana
        if CCAA == 0 or CCAA == 10:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Alicante.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Comunidad Valenciana (Alicante) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Valencia.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Comunidad Valenciana (Valencia) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Castellón.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Comunidad Valenciana (Castellón) unida')

        # Navarra
        if CCAA == 0 or CCAA == 15:
                if TipoEdificio == 0:
                        try:
                                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_NAVARRA.xlsx'
                                df = (pd.read_excel(archivo, usecols= quitar))
                                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                                print ('BBDD Navarra unida')
                        except:
                                print ('BBDD Navarra no se pudo unir porque no posee la referencia catastral')
                elif TipoEdificio != 0 and Arreglo == 1:
                        archivo = Carpeta_arreglo + '\MOD_NAVARRA.xlsx'
                        df = (pd.read_excel(archivo, usecols= quitar))
                        GranBBDD = pd.concat([GranBBDD, df], axis=0)
                        print ('BBDD Navarra unida')

        # La Rioja
        if CCAA == 0 or CCAA == 17:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_RIOJA.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD La Rioja unida')

        # Andalucía
        if CCAA == 0 or CCAA == 1:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Almería.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Almería) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Cádiz.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Cádiz) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Córdoba.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Córdoba) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Granada.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Granada) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Huelva.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Huelva) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Jaén.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Jaén) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Malaga.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Malaga) unida')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Sevilla.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Andalucía (Sevilla) unida')

        # Galicia
        if CCAA == 0 or CCAA == 12:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_GALICIA.xlsx'
                df = (pd.read_excel(archivo, usecols= quitar))
                GranBBDD = pd.concat([GranBBDD, df], axis=0)
                print ('BBDD Galicia unida')


        Size_original = GranBBDD.shape[0]
        print ('La BBDD completa tiene ' + str(Size_original) + ' certificados de edificios')


        if TipoEdificio == 0:
          GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Todos_los_certificados_España_" + Fecha_dato + ".csv", index=False)
          with open(Carpeta_archivos_guardar + r"\Datos_BBDD_Todos_los_certificados_España_" + Fecha_dato + ".txt", 'w') as f:
                f.write('La BBDD completa tiene ' + str(Size_original) + ' certificados de edificios')
        if TipoEdificio == 1:
           GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Residencial_Todos_los_certificados_España_" + Fecha_dato + ".csv", index=False)
           with open(Carpeta_archivos_guardar + r"\Datos_BBDD_Residencial_Todos_los_certificados_España_" + Fecha_dato + ".txt", 'w') as f:
                f.write('La BBDD completa tiene ' + str(Size_original) + ' certificados de edificios (uso residencial)')
        if TipoEdificio == 2:
           GranBBDD.to_csv(Carpeta_archivos_guardar + r"\Terciario_Todos_los_certificados_España_" + Fecha_dato + ".csv", index=False)
           with open(Carpeta_archivos_guardar + r"\Datos_BBDD_Terciario_Todos_los_certificados_España_" + Fecha_dato + ".txt", 'w') as f:
                f.write('La BBDD completa tiene ' + str(Size_original) + ' certificados de edificios (uso terciario)')
        

