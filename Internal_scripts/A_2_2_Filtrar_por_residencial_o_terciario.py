def Filtrar_uso (CCAA, Carpeta_archivos_leer, Fecha_dato):

    # Bibliotecas necesarias
    import os
    import pandas as pd
    import numpy as np
    import xlrd 
    print ('Empieza a filtrarse los datos por uso')

    # Crea la carpeta donde se almacenarán los archivos modificados
    os.makedirs('BBDD_Residencial_Terciario', exist_ok=True)

    carpeta_residencial = 'BBDD_Residencial_Terciario\BBDD_Residencial_' + Fecha_dato
    carpeta_terciario = 'BBDD_Residencial_Terciario\BBDD_Terciario_'+ Fecha_dato

    os.makedirs(carpeta_residencial, exist_ok=True)
    os.makedirs(carpeta_terciario, exist_ok=True)

    # Scripts para eliminar datos erróneos en cada una de las bases de datos
    from Internal_scripts.Scripts_homogeneizar_BBDD import Script_Separar_Residencial_Terciario

    # Crea el informe de número de errores encontrados
    TipoBBDD = pd.DataFrame(columns=('Comunidad autónoma', 'Total de certificados', 'Total de certificados residencial', 'Total de certificados terciario', 'Total de certificados Residencial - Vivienda unifamiliar', 'Residencial - Vivienda individual','Residencial - Bloque completo', 'Terciario - Local', 'Terciario - Edificio completo', 'Terciario - Otros'))


    # Asturias
    if CCAA == 0 or CCAA == 3:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = Carpeta_archivos_leer + r"\MOD_ASTURIAS.xlsx"
        # Ejecuta el script y guarda el resultado
        ccaa = 'Asturias'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ASTURIAS.xlsx", index=False)
        print ('BBDD Asturias residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ASTURIAS.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Asturias terciario creada')

    # Aragón
    if CCAA == 0 or CCAA == 2:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = Carpeta_archivos_leer + r"\MOD_ARAGÓN.xlsx"
        # Ejecuta el script y guarda el resultado
        ccaa = 'Aragón'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ARAGÓN.xlsx", index=False)
        print ('BBDD Aragón residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ARAGÓN.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Aragón terciario creada')

    # Baleares
    if CCAA == 0 or CCAA == 4:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = Carpeta_archivos_leer + r"\MOD_BALEARES.xlsx"
        # Ejecuta el script y guarda el resultado
        ccaa = 'Baleares'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_BALEARES.xlsx", index=False)
        print ('BBDD Baleares residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_BALEARES.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Baleares terciario creada')

    # Canarias
    if CCAA == 0 or CCAA == 5:
        print ('Importante: Canarias no aporta el tipo de edificio, por lo tanto no se puede filtrar')
    # Importante: Canarias no aporta el tipo de edificio, por lo tanto no se puede filtrar porque dará un error

    # Cantabria
    if CCAA == 0 or CCAA == 6:
        print ('Importante: Cantabria no aporta el tipo de edificio, por lo tanto no se puede filtrar')
    # Importante: Cantabria no aporta el tipo de edificio, por lo tanto no se puede filtrar porque dará un error


    # Castilla Y León
    if CCAA == 0 or CCAA == 7:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = Carpeta_archivos_leer + r"\MOD_CYL.xlsx"
        # Ejecuta el script y guarda el resultado
        ccaa = 'Castilla y León'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CYL.xlsx", index=False)
        print ('BBDD Castilla y León residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CYL.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Castilla y León terciario creada')

    # Castilla La Mancha
    if CCAA == 0 or CCAA == 8:
        # Cada provincia por separado: Ruta relativa hasta la BBDD ya homogeneizada, ejecuta el script y guarda el resultado
        archivo = Carpeta_archivos_leer + r"\MOD_CLM_Toledo.xlsx"
        ccaa = 'Castilla La Mancha (Toledo)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CLM_Toledo.xlsx", index=False)
        print ('BBDD Castilla La Mancha (Toledo) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CLM_Toledo.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Castilla La Mancha (Toledo) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_CLM_Guadalajara.xlsx"
        ccaa = 'Castilla La Mancha (Guadalajara)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CLM_Guadalajara.xlsx", index=False)
        print ('BBDD Castilla La Mancha (Guadalajara) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CLM_Guadalajara.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Castilla La Mancha (Guadalajara) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_CLM_Cuenca.xlsx"
        ccaa = 'Castilla La Mancha (Cuenca)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CLM_Cuenca.xlsx", index=False)
        print ('BBDD Castilla La Mancha (Cuenca) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CLM_Cuenca.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Castilla La Mancha (Cuenca) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_CLM_CiudadReal.xlsx"
        ccaa = 'Castilla La Mancha (Ciudad Real)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CLM_CiudadReal.xlsx", index=False)
        print ('BBDD Castilla La Mancha (Ciudad Real) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CLM_CiudadReal.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Castilla La Mancha (Ciudad Real) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_CLM_Albacete.xlsx"
        ccaa = 'Castilla La Mancha (Albacete)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CLM_Albacete.xlsx", index=False)
        print ('BBDD Castilla La Mancha (Albacete) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CLM_Albacete.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Castilla La Mancha (Albacete) terciario creada')

    # Cataluña
    if CCAA == 0 or CCAA == 9:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = Carpeta_archivos_leer + r"\MOD_CATALUÑA.csv"
        # Ejecuta el script y guarda el resultado
        ccaa = 'Cataluña'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_csv(carpeta_residencial + r"\MOD_CATALUÑA.csv", index=False)
        print ('BBDD Cataluña residencial creada')
        df_terciario.to_csv(carpeta_terciario + r"\MOD_CATALUÑA.csv", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Cataluña terciario creada')

    # Comunidad Valenciana
    if CCAA == 0 or CCAA == 10:
        # Cada provincia por separado: Ruta relativa hasta la BBDD ya homogeneizada, ejecuta el script y guarda el resultado
        archivo = Carpeta_archivos_leer + r"\MOD_CVALENCIANA_Alicante.xlsx"
        ccaa = 'Comunidad Valenciana (Alicante)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CVALENCIANA_Alicante.xlsx", index=False)
        print ('BBDD Comunidad Valenciana (Alicante) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CVALENCIANA_Alicante.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Comunidad Valenciana (Alicante) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_CVALENCIANA_Valencia.xlsx"
        ccaa = 'Comunidad Valenciana (Valencia)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CVALENCIANA_Valencia.xlsx", index=False)
        print ('BBDD Comunidad Valenciana (Valencia) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CVALENCIANA_Valencia.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Comunidad Valenciana (Valencia) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_CVALENCIANA_Castellón.xlsx"
        ccaa = 'Comunidad Valenciana (Castellón)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_CVALENCIANA_Castellón.xlsx", index=False)
        print ('BBDD Comunidad Valenciana (Castellón) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_CVALENCIANA_Castellón.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Comunidad Valenciana (Castellón) terciario creada')

    # Navarra
    if CCAA == 0 or CCAA == 15:
        print ('Importante: Navarra no aporta el tipo de edificio, por lo tanto no se puede filtrar')
    # Importante: Navarra no aporta el tipo de edificio, por lo tanto no se puede filtrar porque dará un error

    # La Rioja
    if CCAA == 0 or CCAA == 17:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = Carpeta_archivos_leer + r"\MOD_RIOJA.xlsx"
        # Ejecuta el script y guarda el resultado
        ccaa = 'La Rioja'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_RIOJA.xlsx", index=False)
        print ('BBDD La Rioja residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_RIOJA.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD La Rioja terciario creada')

    # Andalucía
    if CCAA == 0 or CCAA == 1:
        # Cada provincia por separado: Ruta relativa hasta la BBDD ya homogeneizada, ejecuta el script y guarda el resultado
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Almería.xlsx"
        ccaa = 'Andalucía (Almería)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Almería.xlsx", index=False)
        print ('BBDD Andalucía (Almería) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Almería.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Almería) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Cádiz.xlsx"
        ccaa = 'Andalucía (Cádiz)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Cádiz.xlsx", index=False)
        print ('BBDD Andalucía (Cádiz) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Cádiz.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Cádiz) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Córdoba.xlsx"
        ccaa = 'Andalucía (Córdoba)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Córdoba.xlsx", index=False)
        print ('BBDD Andalucía (Córdoba) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Córdoba.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Córdoba) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Granada.xlsx"
        ccaa = 'Andalucía (Granada)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Granada.xlsx", index=False)
        print ('BBDD Andalucía (Granada) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Granada.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Granada) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Huelva.xlsx"
        ccaa = 'Andalucía (Huelva)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Huelva.xlsx", index=False)
        print ('BBDD Andalucía (Huelva) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Huelva.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Huelva) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Jaén.xlsx"
        ccaa = 'Andalucía (Jaén)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Jaén.xlsx", index=False)
        print ('BBDD Andalucía (Jaén) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Jaén.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Jaén) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Malaga.xlsx"
        ccaa = 'Andalucía (Malaga)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Malaga.xlsx", index=False)
        print ('BBDD Andalucía (Malaga) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Malaga.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Malaga) terciario creada')
        archivo = Carpeta_archivos_leer + r"\MOD_ANDALUCÍA_Sevilla.xlsx"
        ccaa = 'Andalucía (Sevilla)'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_ANDALUCÍA_Sevilla.xlsx", index=False)
        print ('BBDD Andalucía (Sevilla) residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_ANDALUCÍA_Sevilla.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Andalucía (Sevilla) terciario creada')

    # Galicia
    if CCAA == 0 or CCAA == 12:
        # Ruta relativa hasta la BBDD ya homogeneizada
        archivo = Carpeta_archivos_leer + r"\MOD_GALICIA.xlsx"
        # Ejecuta el script y guarda el resultado
        ccaa = 'Galicia'
        df_residencial, df_terciario, informe = Script_Separar_Residencial_Terciario.Separar(archivo, ccaa)
        df_residencial.to_excel(carpeta_residencial + r"\MOD_GALICIA.xlsx", index=False)
        print ('BBDD Galicia residencial creada')
        df_terciario.to_excel(carpeta_terciario + r"\MOD_GALICIA.xlsx", index=False)
        TipoBBDD = pd.concat([TipoBBDD, informe], axis=0)
        print ('BBDD Galicia terciario creada')


    TipoBBDD.to_excel(r"BBDD_Residencial_Terciario\Informe_Residencial_Terciario_" + Fecha_dato + ".xlsx", index=False)
