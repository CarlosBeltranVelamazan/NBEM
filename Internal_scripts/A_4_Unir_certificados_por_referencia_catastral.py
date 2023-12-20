# Uno por Referencia catastral los certificados, pongo el nº de certificados de cada CP, su consumo y emisiones medio y mediano y el nº de certificados por letra
# Navarra y País Vasco no están en el catastro con lo que no se pueden unir por Referencia Catastral

def Unir (CCAA, Carpeta_archivos_leer, Certificados_uso, Fecha_dato):

        import os
        import pandas as pd
        import numpy as np
        import xlrd 
        print ("Empieza el proceso de unir por referencia catastral") 

        # Scripts para eliminar datos erróneos en cada una de las bases de datos
        from Internal_scripts.Scripts_Unir_ReferenciaCatastral import Script_Unir_certificados_por_referencia_catastral

        # Crea la carpeta donde se almacenarán los archivos unidos por Referencia Catastral
        os.makedirs('BBDD_Unidas por Referencia Catastral', exist_ok=True)

        # Importante: Certificados a unir por Referencia Catastral. Usar esta variable para escoger si se emplean todos los certificados, sólo los de uso residencial o sólo los de uso terciario. Esta variable define la ruta de entrada de los archivos. Es necesario haber hecho el correspondiente paso en el script de Eliminar datos incorrectos
        # Importante: En la variable TipoEdificio si pones 0 utiliza todos los certificados, si pones 1 utiliza sólo los de uso residencial, si pones 2 utiliza sólo los de uso terciario
        TipoEdificio = Certificados_uso
        print ("Nota: Navarra y País Vasco no están en el catastro con lo que no se pueden unir por referencia catastral")
        if TipoEdificio == 0:
                print ("Estás empleando todos los certificados independientemente de si es residencial o terciario")
                os.makedirs('BBDD_Unidas por Referencia Catastral\Todos los certificados_' + Fecha_dato, exist_ok=True)
        if TipoEdificio == 1:
                print ("Estás empleando los certificados de uso residencial")
                print ("Las BBDD de Canarias, Cantabria y Navarra no aportan este dato y no se tratarán")
                os.makedirs('BBDD_Unidas por Referencia Catastral\Residencial_' + Fecha_dato, exist_ok=True)
        if TipoEdificio == 2:
                print ("Estás empleando los certificados de uso terciario")
                print ("Las BBDD de Canarias, Cantabria y Navarra no aportan este dato y no se tratarán")
                os.makedirs('BBDD_Unidas por Referencia Catastral\Terciario_' + Fecha_dato, exist_ok=True)

        switch_BBDD = {
                0: Carpeta_archivos_leer,
                1: Carpeta_archivos_leer,
                2: Carpeta_archivos_leer}
        switch_BBDD_guardar = {
                0: 'BBDD_Unidas por Referencia Catastral\Todos los certificados_' + Fecha_dato,
                1: 'BBDD_Unidas por Referencia Catastral\Residencial_' + Fecha_dato,
                2: 'BBDD_Unidas por Referencia Catastral\Terciario_' + Fecha_dato}

        # Asturias
        if CCAA == 0 or CCAA == 3:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ASTURIAS.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ASTURIAS.xlsx', index=False)
                print ('BBDD Asturias creada')

        # Aragón
        if CCAA == 0 or CCAA == 2:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ARAGÓN.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ARAGÓN.xlsx', index=False)
                print ('BBDD Aragón creada')

        # Baleares
        if CCAA == 0 or CCAA == 4:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_BALEARES.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) +'\MOD_BALEARES.xlsx', index=False)
                print ('BBDD Baleares creada')

        # Canarias
        if CCAA == 0 or CCAA == 5:
                if TipoEdificio == 0:
                        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CANARIAS.xlsx'
                        df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CANARIAS.xlsx', index=False)
                        print ('BBDD Canarias creada')
                else:
                        print ('BBDD Canarias no da el tipo de edificio')

        # Cantabria
        if CCAA == 0 or CCAA == 6:
                if TipoEdificio == 0:
                        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CANTABRIA.xlsx'
                        df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CANTABRIA.xlsx', index=False)
                        print ('BBDD Cantabria creada')
                else:
                        print ('BBDD Cantabria no da el tipo de edificio')

        # Castilla Y León
        if CCAA == 0 or CCAA == 7:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CYL.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CYL.xlsx', index=False)
                print ('BBDD Castilla y León creada')

        # Castilla La Mancha
        if CCAA == 0 or CCAA == 8:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Toledo.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Toledo.xlsx', index=False)
                print ('BBDD Castilla La Mancha (Toledo) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Guadalajara.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Guadalajara.xlsx', index=False)
                print ('BBDD Castilla La Mancha (Guadalajara) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Cuenca.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Cuenca.xlsx', index=False)
                print ('BBDD Castilla La Mancha (Cuenca) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_CiudadReal.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_CiudadReal.xlsx', index=False)
                print ('BBDD Castilla La Mancha (Ciudad Real) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Albacete.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Albacete.xlsx', index=False)
                print ('BBDD Castilla La Mancha (Albacete) creada')

        # Cataluña
        if CCAA == 0 or CCAA == 9:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CATALUÑA.csv'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_csv(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CATALUÑA.csv', index=False)
                print ('BBDD Cataluña creada')

        # Comunidad Valenciana
        if CCAA == 0 or CCAA == 10:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Alicante.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CVALENCIANA_Alicante.xlsx', index=False)
                print ('BBDD Comunidad Valenciana (Alicante) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Valencia.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CVALENCIANA_Valencia.xlsx', index=False)
                print ('BBDD Comunidad Valenciana (Valencia) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Castellón.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CVALENCIANA_Castellón.xlsx', index=False)
                print ('BBDD Comunidad Valenciana (Castellón) creada')

        # Navarra
        if CCAA == 0 or CCAA == 15:
                print ('BBDD Navarra no está en el catastro')
        #Hacer_esta_BBDD = 0
        #if TipoEdificio == 0:
        #        if Hacer_esta_BBDD == 1 or Hacer_todas_las_BBDD == 1 :
        #                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_NAVARRA.xlsx'
        #                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
        #                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_NAVARRA.xlsx', index=False)
        #                print ('BBDD Navarra creada')

        # La Rioja
        if CCAA == 0 or CCAA == 17:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_RIOJA.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_RIOJA.xlsx', index=False)
                print ('BBDD La Rioja creada')

        # Andalucía
        if CCAA == 0 or CCAA == 1:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Almería.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Almería.xlsx', index=False)
                print ('BBDD Andalucía (Almería) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Cádiz.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Cádiz.xlsx', index=False)
                print ('BBDD Andalucía (Cádiz) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Córdoba.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Córdoba.xlsx', index=False)
                print ('BBDD Andalucía (Córdoba) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Granada.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Granada.xlsx', index=False)
                print ('BBDD Andalucía (Granada) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Huelva.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Huelva.xlsx', index=False)
                print ('BBDD Andalucía (Huelva) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Jaén.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Jaén.xlsx', index=False)
                print ('BBDD Andalucía (Jaén) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Malaga.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Malaga.xlsx', index=False)
                print ('BBDD Andalucía (Malaga) creada')
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Sevilla.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Sevilla.xlsx', index=False)
                print ('BBDD Andalucía (Sevilla) creada')

        # Galicia
        if CCAA == 0 or CCAA == 12:
                archivo = switch_BBDD.get(TipoEdificio) + '\MOD_GALICIA.xlsx'
                df = Script_Unir_certificados_por_referencia_catastral.UnirRefCat(archivo)
                df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_GALICIA.xlsx', index=False)
                print ('BBDD Galicia creada')

