# Este script homogeneiza las BBDD en un formato común para todas
def Homogeneizar (CCAA, Carpeta_archivos_leer, Carpeta_archivos_guardar, Quitar_extras):

    # Bibliotecas necesarias
    import os
    import pandas as pd
    import numpy as np
    import xlrd 
    print ('Empieza el proceso de homogeneizar BBDD')

    # Scripts para homogeneizar cada una de las bases de datos
    from Internal_scripts.Scripts_homogeneizar_BBDD import Crear_tabla_estándar_Asturias, Crear_tabla_estándar_Aragón, Crear_tabla_estándar_Baleares, Crear_tabla_estándar_Canarias, Crear_tabla_estándar_Cantabria, Crear_tabla_estándar_Cataluña, Crear_tabla_estándar_Castilla_La_Mancha, Crear_tabla_estándar_C_Valenciana, Crear_tabla_estándar_Castilla_Y_León, Crear_tabla_estándar_Galicia, Crear_tabla_estándar_Navarra, Crear_tabla_estándar_Rioja, Crear_tabla_estándar_Andalucia

    # Crea la carpeta donde se almacenarán los archivos modificados
    os.makedirs(Carpeta_archivos_guardar, exist_ok=True)

    # Informe para ver el nº de certificados de cada CCAA
    informe_CCAA = pd.DataFrame(columns=('Comunidad autónoma', 'Total de certificados', 'Total de certificados correctos', 'Certificados eliminados por estar duplicados'))

    # Asturias
    if CCAA == 0 or CCAA == 3:
        archivo = Carpeta_archivos_leer + r"\Asturias.xlsx"
        df, duplicados = Crear_tabla_estándar_Asturias.AsturiasDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ASTURIAS.xlsx")
        print ('BBDD Asturias creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Asturias'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Aragón
    if CCAA == 0 or CCAA == 2:
        archivo = Carpeta_archivos_leer + r"\Aragon.xlsx"
        df, duplicados = Crear_tabla_estándar_Aragón.AragónDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ARAGÓN.xlsx")
        print ('BBDD Aragón creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Aragón'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Baleares
    if CCAA == 0 or CCAA == 4:
        archivo = Carpeta_archivos_leer + r"\Baleares.csv"
        df, duplicados = Crear_tabla_estándar_Baleares.BalearesDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar +r"\MOD_BALEARES.xlsx")
        print ('BBDD Baleares creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Baleares'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Canarias
    if CCAA == 0 or CCAA == 5:
        archivo = Carpeta_archivos_leer + r"\rcee122022.csv"
        df, duplicados = Crear_tabla_estándar_Canarias.CanariasDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CANARIAS.xlsx")
        print ('BBDD Canarias creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Canarias'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Cantabria
    if CCAA == 0 or CCAA == 6:
        archivo = Carpeta_archivos_leer + r"\Cantabria.xlsx"
        df, duplicados = Crear_tabla_estándar_Cantabria.CantabriaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CANTABRIA.xlsx")
        print ('BBDD Cantabria creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Cantabria'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Cataluña
    if CCAA == 0 or CCAA == 9:
        archivo = Carpeta_archivos_leer + r"\Cataluña.csv"
        df, duplicados = Crear_tabla_estándar_Cataluña.CataluñaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_csv(Carpeta_archivos_guardar + r"\MOD_CATALUÑA.csv")
        print ('BBDD Cataluña creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Cataluña'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Castilla la Mancha
    if CCAA == 0 or CCAA == 8:
        # Toledo
        archivo = Carpeta_archivos_leer + r"\consulta-scción-1º- toledo-certificadosEEE.xls"
        df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.ToledoDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CLM_Toledo.xlsx")
        print ('BBDD Castilla la Mancha (Toledo) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Toledo)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Guadalajara
        archivo = Carpeta_archivos_leer + r"\consulta-seccion 1º-guadalajara-certificadosEEE.xls"
        df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.GuadalajaraDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CLM_Guadalajara.xlsx")
        print ('BBDD Castilla la Mancha (Guadalajara) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Guadalajara)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Cuenca
        archivo = Carpeta_archivos_leer + r"\consulta-seccion-1º-ceunca-certificadosEEE.xls"
        df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.CuencaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CLM_Cuenca.xlsx")
        print ('BBDD Castilla la Mancha (Cuenca) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Cuenca)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Ciudad Real
        archivo = Carpeta_archivos_leer + r"\consulta-seccion 1º-ciudad real-certificadosEEE.xls"
        df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.CiudadRealDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CLM_CiudadReal.xlsx")
        print ('BBDD Castilla la Mancha (Ciudad Real) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Ciudad Real)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Albacete
        archivo = Carpeta_archivos_leer + r"\Consulta-seccion 1º-albacete-certificadosEEE.xls"
        df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.AlbaceteDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CLM_Albacete.xlsx")
        print ('BBDD Castilla la Mancha (Albacete) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Albacete)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Comunidad Valenciana
    if CCAA == 0 or CCAA == 10:
        # Alicante
        # Las BBDD las dan por año de registro de certificado, hay que unirlas todas para poder tener una base completa de los certificados de cada provincia
        Alicante_BBDD = (r"\CVALENCIANA_Alicante_2013.csv", r"\CVALENCIANA_Alicante_2014.csv", r"\CVALENCIANA_Alicante_2015.csv",
                        r"\CVALENCIANA_Alicante_2016.csv", r"\CVALENCIANA_Alicante_2017.csv", r"\CVALENCIANA_Alicante_2018.csv",
                        r"\CVALENCIANA_Alicante_2019.csv", r"\CVALENCIANA_Alicante_2020.csv", r"\CVALENCIANA_Alicante_2021.csv",
                        r"\CVALENCIANA_Alicante_2022.csv")
        alicanteDB = pd.DataFrame()
        for i in Alicante_BBDD:
            archivo = Carpeta_archivos_leer + i
            df = (pd.read_csv(archivo, skiprows=0, delimiter=';'))
            alicanteDB = pd.concat([alicanteDB, df], axis=0)
        alicanteDB.to_excel(Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Alicante.xlsx")
        archivo = Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Alicante.xlsx"
        df, duplicados = Crear_tabla_estándar_C_Valenciana.AlicanteDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Alicante.xlsx")
        print ('BBDD Comunidad Valenciana (Alicante) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Comunidad Valenciana (Alicante)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Valencia
        Valencia_BBDD = (r"\CVALENCIANA_Valencia_2013.csv", r"\CVALENCIANA_Valencia_2014.csv", r"\CVALENCIANA_Valencia_2015.csv",
                        r"\CVALENCIANA_Valencia_2016.csv", r"\CVALENCIANA_Valencia_2017.csv", r"\CVALENCIANA_Valencia_2018.csv",
                        r"\CVALENCIANA_Valencia_2019.csv", r"\CVALENCIANA_Valencia_2020.csv", r"\CVALENCIANA_Valencia_2021.csv",
                        r"\CVALENCIANA_Valencia_2022.csv")
        ValenciaDB = pd.DataFrame()
        for i in Valencia_BBDD:
            archivo = Carpeta_archivos_leer + i
            df = (pd.read_csv(archivo, skiprows=0, delimiter=';'))
            ValenciaDB = pd.concat([ValenciaDB, df], axis=0)
        ValenciaDB.to_excel(Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Valencia.xlsx")
        archivo = Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Valencia.xlsx"
        df, duplicados = Crear_tabla_estándar_C_Valenciana.ValenciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Valencia.xlsx")
        print ('BBDD Comunidad Valenciana (Valencia) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Comunidad Valenciana (Valencia)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Castellón             Nota: Al unir por años aparece un error en el del año 2014, hay una dirección que tiene un carácter inválido de ser escrito en formato xlsx, un carácter muy raro, hay que borrarlo a mano (está en el certificado con ref catastral E2014VB017159)
        Castellon_BBDD = (r"\CVALENCIANA_Castellon_2013.csv", r"\CVALENCIANA_Castellon_2014.csv", r"\CVALENCIANA_Castellon_2015.csv",
                        r"\CVALENCIANA_Castellon_2016.csv", r"\CVALENCIANA_Castellon_2017.csv", r"\CVALENCIANA_Castellon_2018.csv",
                        r"\CVALENCIANA_Castellon_2019.csv", r"\CVALENCIANA_Castellon_2020.csv", r"\CVALENCIANA_Castellon_2021.csv",
                        r"\CVALENCIANA_Castellon_2022.csv")
        CastellonDB = pd.DataFrame()
        for i in Castellon_BBDD:
            archivo = Carpeta_archivos_leer + i
            df = (pd.read_csv(archivo, skiprows=0, delimiter=';'))
            CastellonDB = pd.concat([CastellonDB, df], axis=0)
        CastellonDB.to_excel(Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Castellón.xlsx")
        archivo = Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Castellón.xlsx"
        df, duplicados = Crear_tabla_estándar_C_Valenciana.CastellónDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CVALENCIANA_Castellón.xlsx")
        print ('BBDD Comunidad Valenciana (Castellón) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Comunidad Valenciana (Castellón)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Castilla y León
    if CCAA == 0 or CCAA == 7:
        archivo = Carpeta_archivos_leer + r"\CYL.xlsx"
        df, duplicados = Crear_tabla_estándar_Castilla_Y_León.CYLDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_CYL.xlsx")
        print ('BBDD Castilla y León creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Castilla y León'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Galicia
    if CCAA == 0 or CCAA == 12:
        archivo = Carpeta_archivos_leer + r"\Galicia.csv"
        df, duplicados = Crear_tabla_estándar_Galicia.GaliciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_GALICIA.xlsx")
        print ('BBDD Galicia creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Galicia'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Navarra       Están reformando la BBDD, hay que adaptar los cambios que hagan. Revisar que el extraer los datos de Energía primaria no renovable y Emisiones de CO2 extraigo un nº de caracterres y puede haber proble,mas importantes con numeros muy pequeños o grandes
    if CCAA == 0 or CCAA == 15:
        archivo = Carpeta_archivos_leer + r"\CNavarra.csv"
        df, duplicados = Crear_tabla_estándar_Navarra.NavarraDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_NAVARRA.xlsx")
        print ('BBDD Navarra creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Navarra'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # La Rioja
    if CCAA == 0 or CCAA == 17:
        archivo = Carpeta_archivos_leer + r"\Rioja.csv"
        df, duplicados = Crear_tabla_estándar_Rioja.RiojaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:49]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_RIOJA.xlsx")
        print ('BBDD La Rioja creada')
        informe = pd.DataFrame({'Comunidad autónoma':['La Rioja'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    # Andalucía
    if CCAA == 0 or CCAA == 1:
        # Almería
        archivo = Carpeta_archivos_leer + r"\Almería.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Almería.xlsx", index=True)
        print ('BBDD Andalucía (Almería) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Almería)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Cádiz
        archivo = Carpeta_archivos_leer + r"\Cádiz.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Cádiz.xlsx")
        print ('BBDD Andalucía (Cádiz) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Cádiz)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Córdoba
        archivo = Carpeta_archivos_leer + r"\Córdoba.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Córdoba.xlsx")
        print ('BBDD Andalucía (Córdoba) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Córdoba)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Granada
        archivo = Carpeta_archivos_leer + r"\Granada.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Granada.xlsx")
        print ('BBDD Andalucía (Granada) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Granada)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Huelva
        archivo = Carpeta_archivos_leer + r"\Huelva.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Huelva.xlsx")
        print ('BBDD Andalucía (Huelva) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Huelva)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Jaén
        archivo = Carpeta_archivos_leer + r"\Jaén.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Jaén.xlsx")
        print ('BBDD Andalucía (Jaén) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Jaén)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Malaga
        archivo = Carpeta_archivos_leer + r"\Malaga.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Malaga.xlsx")
        print ('BBDD Andalucía (Malaga) creada')
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Malaga)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        # Sevilla
        archivo = Carpeta_archivos_leer + r"\Sevilla.xlsx"
        df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo)
        if Quitar_extras == 1:
            df = df[df.columns[0:48]]
        df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Sevilla.xlsx", index=True)
        print ('BBDD Andalucía (Sevilla) creada') 
        informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Sevilla)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
        informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)

    informe_CCAA.to_excel(Carpeta_archivos_guardar + r"\informe_CCAA.xlsx", index=False)



