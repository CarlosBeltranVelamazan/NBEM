 # Pasos para homogeneizar las bases de datos:
 # 1º Utilizar el script Comando principal para obtener cada base de datos homogeneizada
 # 2º Utilizar el script de Eliminar datos incorrectos para quitar todos los que dan errores y dejar todas las bases según los mismos criterios
 # 3º Utilizar el script Unir certificados por referencia catastral o Unir certificados por código postal para obtenerlos por edificio o código postal
 # 4º Utilizar el script Unir código postal por municipio para obtenerlos por municipios

 # Datos incorrectos:
 # Referencias catastrales: Valores null, 0, - y _
 # Código postal: Valores None


def Filtrar_errores (CCAA, Carpeta_archivos_leer, Certificados_uso, Fecha_dato):

    # Bibliotecas necesarias
    import os
    import pandas as pd
    import numpy as np
    import xlrd 
    print ('Empieza el filtrado de errores')

    # Crea la carpeta donde se almacenarán los archivos modificados
    os.makedirs('BBDD_ErroresEliminados', exist_ok=True)

    # Scripts para eliminar datos erróneos en cada una de las bases de datos
    from Internal_scripts.Scripts_eliminar_datos_incorrectos import Script_Datos_incorrectos_Asturias, Script_Datos_incorrectos_Aragón, Script_Datos_incorrectos_Baleares, Script_Datos_incorrectos_Canarias, Script_Datos_incorrectos_Cantabria, Script_Datos_incorrectos_Castilla_Y_León, Script_Datos_incorrectos_Castilla_La_Mancha, Script_Datos_incorrectos_Cataluña, Script_Datos_incorrectos_CValenciana, Script_Datos_incorrectos_Navarra, Script_Datos_incorrectos_Rioja, Script_Datos_incorrectos_Andalucía, Script_Datos_incorrectos_Galicia

    # Importante: Usar esta variable para escoger si se emplean todos los certificados, sólo los de uso residencial o sólo los de uso terciario. Esta variable define la ruta de entrada de los archivos
    # Importante: En la variable TipoEdificio si pones 0 utiliza todos los certificados, si pones 1 utiliza sólo los de uso residencial, si pones 2 utiliza sólo los de uso terciario
    TipoEdificio = Certificados_uso

    if TipoEdificio == 0:
        print ("Estás filtrando errores de todos los certificados independientemente de si es residencial o terciario")
        os.makedirs('BBDD_ErroresEliminados\Todos los certificados_' + Fecha_dato, exist_ok=True)
    if TipoEdificio == 1:
        print ("Estás filtrando errores de los certificados de uso residencial")
        print ("Las BBDD de Canarias, Cantabria y Navarra no aportan este dato y no se tratarán")
        os.makedirs('BBDD_ErroresEliminados\Residencial_' + Fecha_dato, exist_ok=True)
    if TipoEdificio == 2:
        print ("Estás filtrando errores de los certificados de uso terciario")
        print ("Las BBDD de Canarias, Cantabria y Navarra no aportan este dato y no se tratarán")
        os.makedirs('BBDD_ErroresEliminados\Terciario_' + Fecha_dato, exist_ok=True)

    switch_BBDD = {             # Este switch ya no es necesario, lo dejo porque puede ser útil para futuras modificaciones pero la carpeta que debe emplear le viene ya desde A_Script_clave
        0: Carpeta_archivos_leer,
        1: Carpeta_archivos_leer,
        2: Carpeta_archivos_leer}
    switch_BBDD_guardar = {
        0: 'BBDD_ErroresEliminados\Todos los certificados_' + Fecha_dato,
        1: 'BBDD_ErroresEliminados\Residencial_' + Fecha_dato,
        2: 'BBDD_ErroresEliminados\Terciario_' + Fecha_dato}

    # Crea el informe de número de errores encontrados
    erroresBBDD = pd.DataFrame(columns=('Comunidad autónoma', 'Total de certificados', 'Total de certificados correctos', 'Total de certificados borrados', 'Certificados borrados por errores en ReferenciaCatastral', 'Certificados borrados por errores en CP', 'Certificados borrados por errores en FechaConstrucción','Certificados borrados por errores en SuperficieUtil', 'Certificados borrados por errores en Consumo_energía_primaria', 'Certificados borrados por errores en Calificación_consumo_energía', 'Certificados borrados por errores en Emisiones_CO2', 'Certificados borrados por errores en Calificación_emisiones', 'Certificados borrados por errores en Calificación_general_del_edificio', 'Porcentaje EPC correctos', 'Porcentaje EPC con errores'))


    # Asturias
    if CCAA == 0 or CCAA == 3:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ASTURIAS.xlsx'
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0                # Para que el script filtre los certificados con errores en esta columna poner 1, sino ponerle 0
        eliminar_errores_CP = 0
        eliminar_errores_FechaConstrucción = 0
        eliminar_errores_SuperficieUtil = 0
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Ejecuta el script y guarda el resultado
        ccaa = 'Asturias'
        df, errores, fallos = Script_Datos_incorrectos_Asturias.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)

        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos, si filtramos por referencia catastral cambiar el dato entre corchetes por ['index', 'Unnamed: 0']
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass

        # Guarda los resultados que hemos obtenido
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ASTURIAS.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ASTURIAS.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Asturias creada')

    # Aragón
    if CCAA == 0 or CCAA == 2:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ARAGÓN.xlsx'
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0                # Para que el script filtre los certificados con errores en esta columna poner 1, sino ponerle 0
        eliminar_errores_CP = 0                                 # Como Aragón no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_FechaConstrucción = 0
        eliminar_errores_SuperficieUtil = 0
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Ejecuta el script y guarda el resultado
        ccaa = 'Aragón'
        df, errores, fallos = Script_Datos_incorrectos_Aragón.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ARAGÓN.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ARAGÓN.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Aragón creada')

    # Baleares
    if CCAA == 0 or CCAA == 4:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_BALEARES.xlsx'
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0                # Para que el script filtre los certificados con errores en esta columna poner 1, sino ponerle 0
        eliminar_errores_CP = 0
        eliminar_errores_FechaConstrucción = 0
        eliminar_errores_SuperficieUtil = 0
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 0       # Como Baleares no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        eliminar_errores_Calificación_general_del_edificio = 0  # Esta BBDD tendrá una columna más en su informe para reflejar la Calificación General del Edificio, que es la letra que aporta esta comunidad
        # Ejecuta el script y guarda el resultado
        ccaa = 'Baleares'
        df, errores, fallos = Script_Datos_incorrectos_Baleares.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones,eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, eliminar_errores_Calificación_general_del_edificio, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) +'\MOD_BALEARES.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_BALEARES.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Baleares creada')

    # Canarias
    if CCAA == 0 or CCAA == 5:
        if TipoEdificio == 0:
            # Ruta relativa hasta la BBDD ya homogeneizada
            archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CANARIAS.xlsx'
            # Escoger qué errores queremos filtrar en cada BBDD
            eliminar_errores_ReferenciaCatastral = 0                # Para que el script filtre los certificados con errores en esta columna poner 1, sino ponerle 0
            eliminar_errores_CP = 0                                 # Como Canarias no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_FechaConstrucción = 0                  # Como Canarias no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_SuperficieUtil = 0                     # Como Canarias no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_Consumo_energía_primaria = 1
            eliminar_errores_Calificación_consumo_energía = 1
            eliminar_errores_Emisiones_CO2 = 1
            eliminar_errores_Calificación_emisiones = 1
            # Ejecuta el script y guarda el resultado
            ccaa = 'Canarias'
            df, errores, fallos = Script_Datos_incorrectos_Canarias.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
            # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
            try:
                df = df.drop(['Unnamed: 0'], axis=1)
                fallos = fallos.drop(['Unnamed: 0'], axis=1)
            except:
                pass
            df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CANARIAS.xlsx', index=False)
            fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CANARIAS.xlsx', index=False)
            erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
            print ('BBDD Canarias creada')
        else:
            print ('BBDD Canarias no da el tipo de edificio')

    # Cantabria
    if CCAA == 0 or CCAA == 6:
        if TipoEdificio == 0:
            # Ruta relativa hasta la BBDD ya homogeneizada
            archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CANTABRIA.xlsx'
            # Escoger qué errores queremos filtrar en cada BBDD
            eliminar_errores_ReferenciaCatastral = 0
            eliminar_errores_CP = 0                                 
            eliminar_errores_FechaConstrucción = 0                  # Como Cantabria no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_SuperficieUtil = 0                     # Como Cantabria no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_Consumo_energía_primaria = 1
            eliminar_errores_Calificación_consumo_energía = 1
            eliminar_errores_Emisiones_CO2 = 1
            eliminar_errores_Calificación_emisiones = 1
            # Ejecuta el script y guarda el resultado
            ccaa = 'Cantabria'
            df, errores, fallos = Script_Datos_incorrectos_Cantabria.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
            # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
            try:
                df = df.drop(['Unnamed: 0'], axis=1)
                fallos = fallos.drop(['Unnamed: 0'], axis=1)
            except:
                pass
            df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CANTABRIA.xlsx', index=False)
            fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CANTABRIA.xlsx', index=False)
            erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
            print ('BBDD Cantabria creada')
        else:
            print ('BBDD Cantabria no da el tipo de edificio')

    # Castilla Y León
    if CCAA == 0 or CCAA == 7:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CYL.xlsx'
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0
        eliminar_errores_CP = 0                                 
        eliminar_errores_FechaConstrucción = 0                  # Como Castilla y León no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_SuperficieUtil = 0                     # Como Castilla y León no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Ejecuta el script y guarda el resultado
        ccaa = 'Castilla y León'
        df, errores, fallos = Script_Datos_incorrectos_Castilla_Y_León.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CYL.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CYL.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Castilla y León creada')

    # Castilla La Mancha
    if CCAA == 0 or CCAA == 8:
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0
        eliminar_errores_CP = 0                                 
        eliminar_errores_FechaConstrucción = 0                  # Como Castilla La Mancha no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_SuperficieUtil = 0                     # Como Castilla La Mancha no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_Consumo_energía_primaria = 0           # Como Castilla La Mancha no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 0                      # Como Castilla La Mancha no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_Calificación_emisiones = 1
        # Cada provincia por separado: Ruta relativa hasta la BBDD ya homogeneizada, ejecuta el script y guarda el resultado
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Toledo.xlsx'
        ccaa = 'Castilla La Mancha (Toledo)'
        df, errores, fallos = Script_Datos_incorrectos_Castilla_La_Mancha.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Toledo.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CLM_Toledo.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Castilla La Mancha (Toledo) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Guadalajara.xlsx'
        ccaa = 'Castilla La Mancha (Guadalajara)'
        df, errores, fallos = Script_Datos_incorrectos_Castilla_La_Mancha.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Guadalajara.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CLM_Guadalajara.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Castilla La Mancha (Guadalajara) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Cuenca.xlsx'
        ccaa = 'Castilla La Mancha (Cuenca)'
        df, errores, fallos = Script_Datos_incorrectos_Castilla_La_Mancha.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Cuenca.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CLM_Cuenca.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Castilla La Mancha (Cuenca) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_CiudadReal.xlsx'
        ccaa = 'Castilla La Mancha (Ciudad Real)'
        df, errores, fallos = Script_Datos_incorrectos_Castilla_La_Mancha.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_CiudadReal.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CLM_CiudadReal.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Castilla La Mancha (Ciudad Real) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CLM_Albacete.xlsx'
        ccaa = 'Castilla La Mancha (Albacete)'
        df, errores, fallos = Script_Datos_incorrectos_Castilla_La_Mancha.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CLM_Albacete.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CLM_Albacete.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Castilla La Mancha (Albacete) creada')

    # Cataluña
    if CCAA == 0 or CCAA == 9:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CATALUÑA.csv'
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0
        eliminar_errores_CP = 0
        eliminar_errores_FechaConstrucción = 0                  # Como Cataluña no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_SuperficieUtil = 0                     # Cataluña pero aproximandamente 500000 certificados no lo dan
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Ejecuta el script y guarda el resultado
        ccaa = 'Cataluña'
        df, errores, fallos = Script_Datos_incorrectos_Cataluña.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_csv(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CATALUÑA.csv', index=False)
        fallos.to_csv(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CATALUÑA.csv', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Cataluña creada')

    # Comunidad Valenciana
    if CCAA == 0 or CCAA == 10:
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0
        eliminar_errores_CP = 0                                 
        eliminar_errores_FechaConstrucción = 0
        eliminar_errores_SuperficieUtil = 0                     # Como la Comunidad Valenciana no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Cada provincia por separado: Ruta relativa hasta la BBDD ya homogeneizada, ejecuta el script y guarda el resultado
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Alicante.xlsx'
        ccaa = 'Comunidad Valenciana (Alicante)'
        df, errores, fallos = Script_Datos_incorrectos_CValenciana.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CVALENCIANA_Alicante.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CVALENCIANA_Alicante.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Comunidad Valenciana (Alicante) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Valencia.xlsx'
        ccaa = 'Comunidad Valenciana (Valencia)'
        df, errores, fallos = Script_Datos_incorrectos_CValenciana.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CVALENCIANA_Valencia.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CVALENCIANA_Valencia.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Comunidad Valenciana (Valencia) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_CVALENCIANA_Castellón.xlsx'
        ccaa = 'Comunidad Valenciana (Castellón)'
        df, errores, fallos = Script_Datos_incorrectos_CValenciana.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_CVALENCIANA_Castellón.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_CVALENCIANA_Castellón.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Comunidad Valenciana (Castellón) creada')

    # Navarra
    if CCAA == 0 or CCAA == 15:
        if TipoEdificio == 0:
            # Ruta relativa hasta la BBDD ya homogeneizada
            archivo = switch_BBDD.get(TipoEdificio) + '\MOD_NAVARRA.xlsx'
            # Escoger qué errores queremos filtrar en cada BBDD
            eliminar_errores_ReferenciaCatastral = 0                # Como Navarra no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_CP = 0                                 
            eliminar_errores_FechaConstrucción = 0                  # Como Navarra no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_SuperficieUtil = 0                     # Como Navarra no da este dato el valor debe ser 0 o dará resultados negativos
            eliminar_errores_Consumo_energía_primaria = 1
            eliminar_errores_Calificación_consumo_energía = 1
            eliminar_errores_Emisiones_CO2 = 1
            eliminar_errores_Calificación_emisiones = 1
            # Ejecuta el script y guarda el resultado
            ccaa = 'Navarra'
            df, errores, fallos = Script_Datos_incorrectos_Navarra.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
            # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
            try:
                df = df.drop(['Unnamed: 0'], axis=1)
                fallos = fallos.drop(['Unnamed: 0'], axis=1)
            except:
                pass
            df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_NAVARRA.xlsx', index=False)
            fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_NAVARRA.xlsx', index=False)
            erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
            print ('BBDD Navarra creada')
        else:
            print ('BBDD Navarra no da el tipo de edificio')

    # La Rioja
    if CCAA == 0 or CCAA == 17:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_RIOJA.xlsx'
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0
        eliminar_errores_CP = 0                                 # Como La Rioja no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_FechaConstrucción = 0
        eliminar_errores_SuperficieUtil = 0
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Ejecuta el script y guarda el resultado
        ccaa = 'La Rioja'
        df, errores, fallos = Script_Datos_incorrectos_Rioja.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_RIOJA.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_RIOJA.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD La Rioja creada')

    # Andalucía
    if CCAA == 0 or CCAA == 1:
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0
        eliminar_errores_CP = 0                                 
        eliminar_errores_FechaConstrucción = 0
        eliminar_errores_SuperficieUtil = 0
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Cada provincia por separado: Ruta relativa hasta la BBDD ya homogeneizada, ejecuta el script y guarda el resultado
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Almería.xlsx'
        ccaa = 'Andalucía (Almería)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Almería.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Almería.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Almería) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Cádiz.xlsx'
        ccaa = 'Andalucía (Cádiz)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Cádiz.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Cádiz.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Cádiz) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Córdoba.xlsx'
        ccaa = 'Andalucía (Córdoba)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Córdoba.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Córdoba.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Córdoba) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Granada.xlsx'
        ccaa = 'Andalucía (Granada)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Granada.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Granada.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Granada) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Huelva.xlsx'
        ccaa = 'Andalucía (Huelva)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Huelva.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Huelva.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Huelva) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Jaén.xlsx'
        ccaa = 'Andalucía (Jaén)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Jaén.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Jaén.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Jaén) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Malaga.xlsx'
        ccaa = 'Andalucía (Malaga)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Malaga.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Malaga.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Malaga) creada')
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_ANDALUCÍA_Sevilla.xlsx'
        ccaa = 'Andalucía (Sevilla)'
        df, errores, fallos = Script_Datos_incorrectos_Andalucía.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_ANDALUCÍA_Sevilla.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_ANDALUCÍA_Sevilla.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Andalucía (Sevilla) creada')

    # Galicia
    if CCAA == 0 or CCAA == 12:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = switch_BBDD.get(TipoEdificio) + '\MOD_GALICIA.xlsx'
        # Escoger qué errores queremos filtrar en cada BBDD
        eliminar_errores_ReferenciaCatastral = 0
        eliminar_errores_CP = 0
        eliminar_errores_FechaConstrucción = 0                  # Como Galicia no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_SuperficieUtil = 0                     # Como Galicia no da este dato el valor debe ser 0 o dará resultados negativos
        eliminar_errores_Consumo_energía_primaria = 1
        eliminar_errores_Calificación_consumo_energía = 1
        eliminar_errores_Emisiones_CO2 = 1
        eliminar_errores_Calificación_emisiones = 1
        # Ejecuta el script y guarda el resultado
        ccaa = 'Galicia'
        df, errores, fallos = Script_Datos_incorrectos_Galicia.Eliminar_errores(archivo, eliminar_errores_ReferenciaCatastral, eliminar_errores_CP, eliminar_errores_Consumo_energía_primaria, eliminar_errores_Calificación_consumo_energía, eliminar_errores_Emisiones_CO2, eliminar_errores_Calificación_emisiones, eliminar_errores_FechaConstrucción, eliminar_errores_SuperficieUtil, ccaa)
        # El filtrado de errores nos crea algunas columnas de índices, esta es una forma de eliminarlos
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            fallos = fallos.drop(['Unnamed: 0'], axis=1)
        except:
            pass
        df.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\MOD_GALICIA.xlsx', index=False)
        fallos.to_excel(switch_BBDD_guardar.get(TipoEdificio) + '\CertificadosconFallos_MOD_GALICIA.xlsx', index=False)
        erroresBBDD = pd.concat([erroresBBDD, errores], axis=0)
        print ('BBDD Galicia creada')

    if TipoEdificio == 0:
        erroresBBDD.to_excel(r"BBDD_ErroresEliminados\Informe_errores_CCAA_Todos_los_certificados_" + Fecha_dato + ".xlsx", index=False)
    if TipoEdificio == 1:
        erroresBBDD.to_excel(r"BBDD_ErroresEliminados\Informe_errores_CCAA_Uso_Residencial_" + Fecha_dato + ".xlsx", index=False)
    if TipoEdificio == 2:
        erroresBBDD.to_excel(r"BBDD_ErroresEliminados\Informe_errores_CCAA_Uso_Terciario_" + Fecha_dato + ".xlsx", index=False)


