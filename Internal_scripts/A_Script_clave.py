 # Proceso de la información:
 #   - A.1: Manejo de Bases de datos (BBDD) de certificados energéticos en python

 # Este script controla el paso A: Todos los scripts para descargar, homogeneizar, filtrar por tipos, filtrar errores y 
 # unirlos bien por referencia catastral o por código postal

"""  Pasos que controla este script:
   - Descargar las bases de datos de los certificados energéticos de internet
   - Homogeneiza las BBDD en un formato común para todas
   - Filtra por uso: todos los certificados, sólo residenciales o sólo terciarios
   - Filtra por fecha: Anteriores a 2020 o posteriores
   - Elimina certificados con datos incorrectos o anómalos
   - Une los certificados por referencia catastral de edificio de modo que se obtenga un valor por edificio
   - O bien, une por código postal (WIP)
   - Une todas las bases de datos (ya unidas por referencia catastral) en una sola a nivel estatal
   - Una vez unidos los datos en GIS a nivel de municipio los separa por municipio y tipo de municipio para su análisis """

 #         Antes de nada debemos elegir qué queremos analizar, para ello hay una lista de decisiones, esta lista controla qué resultados obtendremos
def EPCs (folder_read_EPC, folder_save_EPC_modificed, CCAA, Descargar_BBDD, Homogeneizar_BBDD, Fecha_BBDD, Fecha_filtro, Certificados_fecha_que_uso, Uso_BBDD, Certificados_uso, Detectar_errores, 
                  Unir_RefCat, CEE_unidos_por_edificio, Unir_BBDD_España, Separar_en_edif_BI_RefCat):

    # Lista_decisiones:
    Quitar_extras = 0                    # No tocar. Ya no hace nada, al agrupar para quitar los EPC duplicados esto ya no influye, quito las extra siempre. Si quiero quitar las celdas extras para quedarme con las 50 columnas de la tabla homogénea (los campos que daban las CCAA y no estaban en la tabla homogñenea se quedan al final). Solo tabla homogénea (1), todos los valores (0)
    Unir_CP = False                      # No tocar. Ya no hace nada. Si quiero unir los certificados por código postal (True o False) (Work In Progress, dejar en False como hay CP repetidos en diferentes municipios se duplican los resultados)
    grafica_EPC_entrada = False          # Para sacar el nº de EPC que se han presentado cada año

    # Paso 0, ¿quieres descargar los archivos nuevos? Marcar True para descargar, False para trabajar con los que ya hay

    Carpeta_archivos_descargas = folder_read_EPC  # La carpeta donde se guardarán los nuevos archivos descargados

    """ Notas: Se puede descargar unicamente la base de datos (BBDD) de una sola Comunidad Autónoma, para ello entrar al script correspondiente y marcar 
    con un 0 la variable Hacer_todas_las_BBDD y con un 1 la de la CCAA que quieres hacer """

    """ Notas: El script A_0_Descarga_archivos descarga todas las BBDD menos Asturias (hay un problema con un protocolo porque la web es vieja, hay que usar 
    Internet explorer para descargar el archivo) y Galicia (tiene un capcha de No soy un robot y sí soy un robot así que lo he dejado estar)
    Para descargar la BBDD de asturias ir a: https://datos.gob.es/es/catalogo/a03002951-eficiencia-energetica-edif-viv 
    Para Galicia ir a: https://datos.gob.es/es/catalogo/a12002994-registro-de-certificados-de-eficiencia-energetica-de-edificios-de-galicia """

    """ Notas: Ya ha sucedido que con el tiempo cambian los formatos y los encodings de los archivos, puede suceder, unicamente indicar que:
    - La base de datos de Castellón de 2014 tiene un carácter que no es válido en excel y da problemas, lo mejor es eliminarlo a mano, hay que abrirlo 
    con el bloc de notas, está en la dirección del certificado con ref catastral E2014VB017159, hay que abrir el archivo y borrarlo de la dirección. 
    Es el carácter que está justo detrás del PT8 en la dirección, con quitarlo ya funciona bien.
    - Navarra está en proceso de reforma de la BBDD con lo que seguramente tenga cambios
    - Castilla y León da un xls raro, lo mejor es abrirlo con excel o similar y guardarlo en xlsx (revisar que los valores de energía primaria, CO2 y tal los lee como fechas del xls, poner en formato número)
    - Castilla la Mancha y Canarias dan un zip hay que extraerlo
    - Galicia da un csv con problemas por las , de la dirección, eso está ya resuelto en el propio código ya hecho, no hay que hacer nada
    - Andalucía da un xml que da problemas, hay que abrirlo y guardarlo en excel, esto genera que se cuadrupliquen los certificados por un problema con 
    las etiquetas pero el cógido ya implementado lo resuelve y queda toda la información bien. """

    # Paso 1, Homogeneizar las BBDD en un formato común para todas

    Carpeta_archivos_leer = Carpeta_archivos_descargas   # La carpeta de donde se leerán los archivos
    Carpeta_archivos_guardar = folder_save_EPC_modificed        # La carpeta donde se guardarán los nuevos archivos

    # Paso 2-1, Filtra por fecha del certificado, anterior, posterior o todos

    """  En este punto debe indicarse qué certificados queremos usar en los siguientes pasos, para ello poner en la variable Certificados_que_uso, un 0, 1 o 2
    Certificados_fecha_que_uso = 0 se usarán todos los certificados, sin filtrar
    Certificados_fecha_que_uso = 1 se usarán los certificados anteriores al 1/1/2020 (o fecha indicada)
    Certificados_fecha_que_uso = 2 se usarán los certificados posteriores al 1/1/2020 (o fecha indicada)
    Certificados_fecha_que_uso = Cualquier otro número se usarán todos los certificados, sin filtrar (opción por defecto) """

    # Paso 2-2, Filtra por uso: todos los certificados, sólo residenciales o sólo terciarios

    """  En este punto debe indicarse qué certificados queremos usar en los siguientes pasos, para ello poner en la variable Certificados_que_uso, un 0, 1 o 2
    Certificados_uso = 0 se usarán todos los certificados, sin filtrar
    Certificados_uso = 1 se usarán los certificados de uso residencial
    Certificados_uso = 2 se usarán los certificados de uso terciario
    Certificados_uso = Cualquier otro número se usarán todos los certificados, sin filtrar (opción por defecto) """

    # Paso 3, Elimina certificados con datos incorrectos o anómalos

    # Paso 4, Une los certificados por referencia catastral de edificio de modo que se obtenga un valor por edificio

    # Paso 5, Une todas las bases de datos (ya unidas por referencia catastral) en una sola a nivel estatal



    # A partir de este punto se ejecuta el código paso a paso (No tocar)

    print ('Empieza el paso A')

    import os
    from time import time
    inicio  = time()

    # Scripts para homogeneizar cada una de las bases de datos
    if Descargar_BBDD == True:
        from Internal_scripts import A_0_Descarga_archivos
        A_0_Descarga_archivos.Descargar (CCAA, Carpeta_archivos_descargas)
        print ('Ver apartado de notas en A_Script_clave para resolver algunas cuestiones de las BBDD descargadas')
    duracion_A_0 = time() - inicio
    print('El paso A.1_0 ha tardado: ' + str(duracion_A_0) + ' segundos')

    if Homogeneizar_BBDD == True:
        from Internal_scripts import A_1_Comando_principal
        A_1_Comando_principal.Homogeneizar (CCAA, Carpeta_archivos_leer, Carpeta_archivos_guardar, Quitar_extras)
    duracion_A_1 = time() - inicio
    print('El paso A.1_1 ha tardado: ' + str(duracion_A_1 - duracion_A_0) + ' segundos')

    if Fecha_BBDD  == True:
        Carpeta_archivos_leer = Carpeta_archivos_guardar
        from Internal_scripts import A_2_1_Filtrar_por_fecha
        A_2_1_Filtrar_por_fecha.Filtrar_fecha (CCAA, Fecha_filtro, Carpeta_archivos_leer)
    duracion_A_2_1 = time() - inicio
    print('El paso A.1_2_1 ha tardado: ' + str(duracion_A_2_1 - duracion_A_1) + ' segundos')

    if Certificados_fecha_que_uso == 1: # Con esta modificación distingue entre si el conjunto escogido es anterior o posterior a la fecha
        Fecha_dato = 'Pre_' + str(Fecha_filtro + 1)
    elif Certificados_fecha_que_uso == 2:
        Fecha_dato = 'Post_' + str(Fecha_filtro + 1)
    else:
        Fecha_dato = 'Todos'

    if Uso_BBDD == True:
        print ('Canarias, Cantabria y Navarra no dan el tipo de edificio, en solo los residenciales o terciarios estas no aparecerán')
        if Certificados_fecha_que_uso == 1:
            Carpeta_archivos_leer = 'Separados_por_fecha\BBDD_Anteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
        elif Certificados_fecha_que_uso == 2:
            Carpeta_archivos_leer = 'Separados_por_fecha\Posteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
        else:
            Carpeta_archivos_leer = Carpeta_archivos_guardar # Por defecto 'BBDD_Modificadas'
        from Internal_scripts import A_2_2_Filtrar_por_residencial_o_terciario
        A_2_2_Filtrar_por_residencial_o_terciario.Filtrar_uso (CCAA, Carpeta_archivos_leer, Fecha_dato)
    duracion_A_2_2 = time() - inicio
    print('El paso A.1_2_2 ha tardado: ' + str(duracion_A_2_2 - duracion_A_2_1) + ' segundos')

    if Detectar_errores == True:
        print ('Canarias, Cantabria y Navarra no dan el tipo de edificio, si se filtran solo los residenciales o terciarios estas no aparecerán')
        if Certificados_fecha_que_uso == 1:
            Carpeta_archivos_leer = 'Separados_por_fecha\BBDD_Anteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
        elif Certificados_fecha_que_uso == 2:
            Carpeta_archivos_leer = 'Separados_por_fecha\Posteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
        else:
            Carpeta_archivos_leer = Carpeta_archivos_guardar # Por defecto 'BBDD_Modificadas'
        if Certificados_uso == 1:
            Carpeta_archivos_leer = 'BBDD_Residencial_Terciario\BBDD_Residencial_'  + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_2_Filtrar_por_residencial_o_terciario
        elif Certificados_uso == 2:
            Carpeta_archivos_leer = 'BBDD_Residencial_Terciario\BBDD_Terciario_'  + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_2_Filtrar_por_residencial_o_terciario
        from Internal_scripts import A_3_Eliminar_datos_incorrectos
        A_3_Eliminar_datos_incorrectos.Filtrar_errores (CCAA, Carpeta_archivos_leer, Certificados_uso, Fecha_dato)
    duracion_A_3 = time() - inicio
    print('El paso A.1_3 ha tardado: ' + str(duracion_A_3 - duracion_A_2_2) + ' segundos')

    if Unir_RefCat == True:
        try:
            if Certificados_uso == 0:
                Carpeta_archivos_leer = 'BBDD_ErroresEliminados\Todos los certificados_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            elif Certificados_uso == 1:
                Carpeta_archivos_leer = 'BBDD_ErroresEliminados\Residencial_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            elif Certificados_uso == 2:
                Carpeta_archivos_leer = 'BBDD_ErroresEliminados\Terciario_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
        except:
            if Certificados_fecha_que_uso == 1:
                Carpeta_archivos_leer = 'Separados_por_fecha\BBDD_Anteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            elif Certificados_fecha_que_uso == 2:
                Carpeta_archivos_leer = 'Separados_por_fecha\Posteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            else:
                Carpeta_archivos_leer = Carpeta_archivos_guardar # Por defecto 'BBDD_Modificadas'
            if Certificados_uso == 1:
                Carpeta_archivos_leer = 'BBDD_Residencial_Terciario\BBDD_Residencial_'  + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_2_Filtrar_por_residencial_o_terciario
            elif Certificados_uso == 2:
                Carpeta_archivos_leer = 'BBDD_Residencial_Terciario\BBDD_Terciario_'  + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_2_Filtrar_por_residencial_o_terciario

        from Internal_scripts import A_4_Unir_certificados_por_referencia_catastral
        A_4_Unir_certificados_por_referencia_catastral.Unir (CCAA, Carpeta_archivos_leer, Certificados_uso, Fecha_dato)
    duracion_A_4 = time() - inicio
    print('El paso A.1_4 ha tardado: ' + str(duracion_A_4 - duracion_A_3) + ' segundos')

    if Unir_CP == True:
        print ('Todavía no se puede hacer, está en proceso')

    # Crea la carpeta donde se almacenarán los archivos unidos por Referencia Catastral
    os.makedirs('BBDD_Unidas por Referencia Catastral', exist_ok=True)
    Carpeta_archivos_guardar = 'BBDD_Unidas por Referencia Catastral'
    if Unir_BBDD_España == True:
        if CEE_unidos_por_edificio == 1:
            if Certificados_uso == 0:
                Carpeta_archivos_leer = 'BBDD_Unidas por Referencia Catastral\Todos los certificados_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            elif Certificados_uso == 1:
                Carpeta_archivos_leer = 'BBDD_Unidas por Referencia Catastral\Residencial_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            elif Certificados_uso == 2:
                Carpeta_archivos_leer = 'BBDD_Unidas por Referencia Catastral\Terciario_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            from Internal_scripts import A_5_Unir_certificados_todas_las_BBDD_de_certificados
            A_5_Unir_certificados_todas_las_BBDD_de_certificados.Unir_BBDD (CCAA, Carpeta_archivos_leer, Carpeta_archivos_guardar, Certificados_uso, Fecha_dato, CEE_unidos_por_edificio)

        elif CEE_unidos_por_edificio == 0:
            try:
                if Certificados_uso == 0:
                    Carpeta_archivos_leer = 'BBDD_ErroresEliminados\Todos los certificados_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
                elif Certificados_uso == 1:
                    Carpeta_archivos_leer = 'BBDD_ErroresEliminados\Residencial_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
                elif Certificados_uso == 2:
                    Carpeta_archivos_leer = 'BBDD_ErroresEliminados\Terciario_' + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
            except:
                if Certificados_fecha_que_uso == 1:
                    Carpeta_archivos_leer = 'Separados_por_fecha\BBDD_Anteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
                elif Certificados_fecha_que_uso == 2:
                    Carpeta_archivos_leer = 'Separados_por_fecha\Posteriores_a_1_1_' + str(Fecha_filtro + 1) # No cambiar esta ruta, o redefinir también en A_2_1_Filtrar_por_fecha
                else:
                    Carpeta_archivos_leer = Carpeta_archivos_guardar # Por defecto 'BBDD_Modificadas'
                if Certificados_uso == 1:
                    Carpeta_archivos_leer = 'BBDD_Residencial_Terciario\BBDD_Residencial_'  + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_2_Filtrar_por_residencial_o_terciario
                elif Certificados_uso == 2:
                    Carpeta_archivos_leer = 'BBDD_Residencial_Terciario\BBDD_Terciario_'  + Fecha_dato # No cambiar esta ruta, o redefinir también en A_2_2_Filtrar_por_residencial_o_terciario
            from Internal_scripts import A_5_Unir_certificados_todas_las_BBDD_de_certificados
            A_5_Unir_certificados_todas_las_BBDD_de_certificados.Unir_BBDD (CCAA, Carpeta_archivos_leer, Carpeta_archivos_guardar, Certificados_uso, Fecha_dato, CEE_unidos_por_edificio)
    duracion_A_5 = time() - inicio
    print('El paso A.1_5 ha tardado: ' + str(duracion_A_5 - duracion_A_4) + ' segundos')


    if Separar_en_edif_BI_RefCat == True:

        Carpeta_archivos_leer = Carpeta_archivos_guardar
        Carpeta_archivos_guardar = Carpeta_archivos_leer + "\\Parquet"
        os.makedirs(Carpeta_archivos_guardar, exist_ok=True)
        file = r"\Todos_los_certificados_España_" + Fecha_dato + ".csv"
        from Internal_scripts import A_6_BBDD_de_certificados_sueltos_escala_BI_y_escala_edificio_separadas
        A_6_BBDD_de_certificados_sueltos_escala_BI_y_escala_edificio_separadas.Separar_14_y_20_difitos_RefCat (Carpeta_archivos_leer, Carpeta_archivos_guardar, file, Certificados_uso)

    duracion_A = time() - inicio
    print('El paso A.1_6 ha tardado: ' + str(duracion_A - duracion_A_5) + ' segundos')

    print ('En total el proceso A.1 (EPC) ha tardado: ' + str(duracion_A) + ' segundos\n'
        #    + 'El paso A.1_0 ha sido: ' + str(duracion_A_0) + ' segundos\n'
        #    + 'El paso A.1_1 ha sido: ' + str(duracion_A_1 - duracion_A_0) + ' segundos\n'
        #    + 'El paso A.1_2_1 ha sido: ' + str(duracion_A_2_1 - duracion_A_1) + ' segundos\n'
        #    + 'El paso A.1_2_2 ha sido: ' + str(duracion_A_2_2 - duracion_A_2_1) + ' segundos\n'
        #    + 'El paso A.1_3 ha sido: ' + str(duracion_A_3 - duracion_A_2_2) + ' segundos\n'
        #    + 'El paso A.1_4 ha sido: ' + str(duracion_A_4 - duracion_A_3) + ' segundos\n'
        #    + 'El paso A.1_5 ha sido: ' + str(duracion_A_5 - duracion_A_4) + ' segundos\n'
        #    + 'El paso A.1_6 ha sido: ' + str(duracion_A - duracion_A_5) + ' segundos\n'
        )
    with open('Time_consumption_Step_A_1_EPCs' + ".txt", 'w') as f:
            f.write('En total el proceso A.1 (EPC) ha tardado: ' + str(duracion_A) + ' segundos\n'
        + 'El paso A.1_0 ha sido: ' + str(duracion_A_0) + ' segundos\n'
        + 'El paso A.1_1 ha sido: ' + str(duracion_A_1 - duracion_A_0) + ' segundos\n'
        + 'El paso A.1_2_1 ha sido: ' + str(duracion_A_2_1 - duracion_A_1) + ' segundos\n'
        + 'El paso A.1_2_2 ha sido: ' + str(duracion_A_2_2 - duracion_A_2_1) + ' segundos\n'
        + 'El paso A.1_3 ha sido: ' + str(duracion_A_3 - duracion_A_2_2) + ' segundos\n'
        + 'El paso A.1_4 ha sido: ' + str(duracion_A_4 - duracion_A_3) + ' segundos\n'
        + 'El paso A.1_5 ha sido: ' + str(duracion_A_5 - duracion_A_4) + ' segundos\n'
        + 'El paso A.1_6 ha sido: ' + str(duracion_A - duracion_A_5) + ' segundos\n'
                    )

    if grafica_EPC_entrada == True:
        from Internal_scripts import F_11_EPC_inscritos_por_año
        Carpeta_archivos_descargas = folder_read_EPC  # La carpeta donde se guardarán los nuevos archivos descargados
        Carpeta_archivos_leer = Carpeta_archivos_descargas   # La carpeta de donde se leerán los archivos
        Carpeta_archivos_guardar = 'Información_Complementaria'        # La carpeta donde se guardarán los nuevos archivos
        os.makedirs(Carpeta_archivos_guardar, exist_ok=True)
        F_11_EPC_inscritos_por_año.Homogeneizar (CCAA, Carpeta_archivos_leer, Carpeta_archivos_guardar, Quitar_extras)




    print ('Terminado todo el paso A.1')
    print ('Step A.1 Completed')

