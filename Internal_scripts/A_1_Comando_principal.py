# Este script homogeneiza las BBDD en un formato común para todas
# Function to remove illegal characters from file
def remove_illegal_characters(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        cleaned_text = text.replace('§', '').replace(chr(21), '')   # Replace § with an empty string or any other suitable character
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)

def Homogeneizar (CCAA, Carpeta_archivos_leer, Carpeta_archivos_guardar, Quitar_extras):

    # Bibliotecas necesarias
    import os
    import pandas as pd
    import numpy as np
    import xlrd 
    print ('Empieza el proceso de homogeneizar BBDD')

    # Scripts para homogeneizar cada una de las bases de datos
    from Internal_scripts.Scripts_homogeneizar_BBDD import Crear_tabla_estándar_Asturias, Crear_tabla_estándar_Aragón, Crear_tabla_estándar_Baleares, Crear_tabla_estándar_Canarias, Crear_tabla_estándar_Cantabria, Crear_tabla_estándar_Cataluña, Crear_tabla_estándar_Castilla_La_Mancha, Crear_tabla_estándar_C_Valenciana, Crear_tabla_estándar_Castilla_Y_León, Crear_tabla_estándar_Galicia, Crear_tabla_estándar_Navarra, Crear_tabla_estándar_Rioja, Crear_tabla_estándar_Andalucia, Crear_tabla_estándar_Andalucia_xmlversion

    # Crea la carpeta donde se almacenarán los archivos modificados
    os.makedirs(Carpeta_archivos_guardar, exist_ok=True)

    # Informe para ver el nº de certificados de cada CCAA
    informe_CCAA = pd.DataFrame(columns=('Comunidad autónoma', 'Total de certificados', 'Total de certificados correctos', 'Certificados eliminados por estar duplicados'))

    # Asturias
    if CCAA == 0 or CCAA == 3:
        try:
            archivo = Carpeta_archivos_leer + r"\Asturias.xlsx"
            df, duplicados = Crear_tabla_estándar_Asturias.AsturiasDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ASTURIAS.xlsx")
            print ('BBDD Asturias creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Asturias'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Asturias')
    
    # Aragón
    if CCAA == 0 or CCAA == 2:
        try:
            archivo = Carpeta_archivos_leer + r"\Aragon.xlsx"
            df, duplicados = Crear_tabla_estándar_Aragón.AragónDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ARAGÓN.xlsx")
            print ('BBDD Aragón creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Aragón'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Aragón')

    # Baleares
    if CCAA == 0 or CCAA == 4:
        try:
            archivo = Carpeta_archivos_leer + r"\Baleares.csv"
            df, duplicados = Crear_tabla_estándar_Baleares.BalearesDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar +r"\MOD_BALEARES.xlsx")
            print ('BBDD Baleares creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Baleares'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Baleares')

    # Canarias
    if CCAA == 0 or CCAA == 5:
        try:
            archivo = Carpeta_archivos_leer + r"\Canarias.csv"
            df, duplicados = Crear_tabla_estándar_Canarias.CanariasDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_CANARIAS.xlsx")
            print ('BBDD Canarias creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Canarias'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Canarias')

    # Cantabria
    if CCAA == 0 or CCAA == 6:
        try:
            archivo = Carpeta_archivos_leer + r"\Cantabria.xlsx"
            df, duplicados = Crear_tabla_estándar_Cantabria.CantabriaDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_CANTABRIA.xlsx")
            print ('BBDD Cantabria creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Cantabria'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
            print ('No hay datos de Cantabria')

    # Cataluña
    if CCAA == 0 or CCAA == 9:
        try:
            archivo = Carpeta_archivos_leer + r"\Cataluña.csv"
            df, duplicados = Crear_tabla_estándar_Cataluña.CataluñaDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_csv(Carpeta_archivos_guardar + r"\MOD_CATALUÑA.csv")
            print ('BBDD Cataluña creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Cataluña'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Cataluña')

    # Castilla la Mancha
    if CCAA == 0 or CCAA == 8:
        try:
            # Toledo
            archivo = Carpeta_archivos_leer + r"\CertificadosEEE_Toledo A-O.xlsx"
            archivo2 = Carpeta_archivos_leer + r"\CertificadosEEE_Toledo P-Z.xlsx"
            df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.ToledoDB(archivo)
            df = df.reset_index()
            df2, duplicados2 = Crear_tabla_estándar_Castilla_La_Mancha.ToledoDB(archivo2)
            df2 = df2.reset_index()
            df = pd.concat([df, df2], axis=0, ignore_index=True)
            duplicados = duplicados + duplicados2
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_csv(Carpeta_archivos_guardar + r"\MOD_CLM_Toledo.csv")
            print ('BBDD Castilla la Mancha (Toledo) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Toledo)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Guadalajara
            archivo = Carpeta_archivos_leer + r"\CertificadosEEE_Guadalajara A-G.xlsx"
            archivo2 = Carpeta_archivos_leer + r"\CertificadosEEE_Guadalajara H-Z.xlsx"
            df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.GuadalajaraDB(archivo)
            df = df.reset_index()
            df2, duplicados2 = Crear_tabla_estándar_Castilla_La_Mancha.GuadalajaraDB(archivo2)
            df2 = df2.reset_index()
            df = pd.concat([df, df2], axis=0, ignore_index=True)
            duplicados = duplicados + duplicados2
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_csv(Carpeta_archivos_guardar + r"\MOD_CLM_Guadalajara.csv")
            print ('BBDD Castilla la Mancha (Guadalajara) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Guadalajara)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Cuenca
            archivo = Carpeta_archivos_leer + r"\CertificadosEEE_Cuenca A-E.xlsx"
            archivo2 = Carpeta_archivos_leer + r"\CertificadosEEE_Cuenca F-Z.xlsx"
            df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.CuencaDB(archivo)
            df = df.reset_index()
            df2, duplicados2 = Crear_tabla_estándar_Castilla_La_Mancha.CuencaDB(archivo2)
            df2 = df2.reset_index()
            df = pd.concat([df, df2], axis=0, ignore_index=True)
            duplicados = duplicados + duplicados2
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_csv(Carpeta_archivos_guardar + r"\MOD_CLM_Cuenca.csv")
            print ('BBDD Castilla la Mancha (Cuenca) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Cuenca)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Ciudad Real
            archivo = Carpeta_archivos_leer + r"\CertificadosEEE_Ciudad_Real A-D.xlsx"
            archivo2 = Carpeta_archivos_leer + r"\CertificadosEEE_Ciudad_Real E-Z.xlsx"
            df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.CiudadRealDB(archivo)
            df = df.reset_index()
            df2, duplicados2 = Crear_tabla_estándar_Castilla_La_Mancha.CiudadRealDB(archivo2)
            df2 = df2.reset_index()
            df = pd.concat([df, df2], axis=0, ignore_index=True)
            duplicados = duplicados + duplicados2
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_csv(Carpeta_archivos_guardar + r"\MOD_CLM_CiudadReal.csv")
            print ('BBDD Castilla la Mancha (Ciudad Real) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Ciudad Real)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Albacete
            archivo = Carpeta_archivos_leer + r"\CertificadosEEE_Albacete A.xlsx"
            archivo2 = Carpeta_archivos_leer + r"\CertificadosEEE_Albacete B-Z.xlsx"
            df, duplicados = Crear_tabla_estándar_Castilla_La_Mancha.AlbaceteDB(archivo)
            df = df.reset_index()
            df2, duplicados2 = Crear_tabla_estándar_Castilla_La_Mancha.AlbaceteDB(archivo2)
            df2 = df2.reset_index()
            df = pd.concat([df, df2], axis=0, ignore_index=True)
            duplicados = duplicados + duplicados2
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_csv(Carpeta_archivos_guardar + r"\MOD_CLM_Albacete.csv")
            print ('BBDD Castilla la Mancha (Albacete) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Castilla la Mancha (Albacete)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
            print ('No hay datos de Castilla la Mancha o alguna provincia')

    # Comunidad Valenciana
    if CCAA == 0 or CCAA == 10:
        #try:
            # Alicante
            # Las BBDD las dan por año de registro de certificado, hay que unirlas todas para poder tener una base completa de los certificados de cada provincia
            Alicante_BBDD = (r"\CVALENCIANA_Alicante_2013.csv", r"\CVALENCIANA_Alicante_2014.csv", r"\CVALENCIANA_Alicante_2015.csv",
                            r"\CVALENCIANA_Alicante_2016.csv", r"\CVALENCIANA_Alicante_2017.csv", r"\CVALENCIANA_Alicante_2018.csv",
                            r"\CVALENCIANA_Alicante_2019.csv", r"\CVALENCIANA_Alicante_2020.csv", r"\CVALENCIANA_Alicante_2021.csv",
                            r"\CVALENCIANA_Alicante_2022.csv", r"\CVALENCIANA_Alicante_2023.csv")
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
                            r"\CVALENCIANA_Valencia_2022.csv", r"\CVALENCIANA_Valencia_2023.csv")
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
                            r"\CVALENCIANA_Castellon_2022.csv", r"\CVALENCIANA_Castellon_2023.csv")
            CastellonDB = pd.DataFrame()
            for i in Castellon_BBDD:
                archivo = Carpeta_archivos_leer + i
                remove_illegal_characters(archivo)                             # Remove illegal characters from each file
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
        #except:
                #print ('No hay datos de la Comunidad Valenciana o alguna provincia') 

    # Castilla y León
    if CCAA == 0 or CCAA == 7:
        try:
            archivo = Carpeta_archivos_leer + r"\CYL.csv"
            df, duplicados = Crear_tabla_estándar_Castilla_Y_León.CYLDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_csv(Carpeta_archivos_guardar + r"\MOD_CYL.csv")
            print ('BBDD Castilla y León creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Castilla y León'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Castilla y León') 

    # Galicia
    if CCAA == 0 or CCAA == 12:
        try:
            archivo = Carpeta_archivos_leer + r"\Galicia.csv"
            df, duplicados = Crear_tabla_estándar_Galicia.GaliciaDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_GALICIA.xlsx")
            print ('BBDD Galicia creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Galicia'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Galicia') 

    # Navarra       Están reformando la BBDD, hay que adaptar los cambios que hagan. Revisar que el extraer los datos de Energía primaria no renovable y Emisiones de CO2 extraigo un nº de caracterres y puede haber proble,mas importantes con numeros muy pequeños o grandes
    if CCAA == 0 or CCAA == 15:
        try:
            archivo = Carpeta_archivos_leer + r"\CNavarra.csv"
            df, duplicados = Crear_tabla_estándar_Navarra.NavarraDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_NAVARRA.xlsx")
            print ('BBDD Navarra creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Navarra'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Navarra') 

    # La Rioja
    if CCAA == 0 or CCAA == 17:
        try:
            archivo = Carpeta_archivos_leer + r"\Rioja.csv"
            df, duplicados = Crear_tabla_estándar_Rioja.RiojaDB(archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:49]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_RIOJA.xlsx")
            print ('BBDD La Rioja creada')
            informe = pd.DataFrame({'Comunidad autónoma':['La Rioja'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de La Rioja') 

    # Andalucía
    if CCAA == 0 or CCAA == 1:
        try:
            # Almería
            archivo = Carpeta_archivos_leer + r"\ALMERIA.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Almería.xlsx", index=True)
            print ('BBDD Andalucía (Almería) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Almería)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Cádiz
            archivo = Carpeta_archivos_leer + r"\CADIZ.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Cádiz.xlsx")
            print ('BBDD Andalucía (Cádiz) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Cádiz)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Córdoba
            archivo = Carpeta_archivos_leer + r"\CORDOBA.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Córdoba.xlsx")
            print ('BBDD Andalucía (Córdoba) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Córdoba)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Granada
            archivo = Carpeta_archivos_leer + r"\GRANADA.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Granada.xlsx")
            print ('BBDD Andalucía (Granada) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Granada)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Huelva
            archivo = Carpeta_archivos_leer + r"\HUELVA.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Huelva.xlsx")
            print ('BBDD Andalucía (Huelva) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Huelva)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Jaén
            archivo = Carpeta_archivos_leer + r"\JAEN.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Jaén.xlsx")
            print ('BBDD Andalucía (Jaén) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Jaén)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Malaga
            archivo = Carpeta_archivos_leer + r"\MALAGA.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Malaga.xlsx")
            print ('BBDD Andalucía (Malaga) creada')
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Malaga)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
            # Sevilla
            archivo = Carpeta_archivos_leer + r"\SEVILLA.xml"
            archivo_xlsx = Crear_tabla_estándar_Andalucia_xmlversion.xml_to_xlsx(archivo)
            df, duplicados = Crear_tabla_estándar_Andalucia.AndaluciaDB(archivo_xlsx, archivo)
            if Quitar_extras == 1:
                df = df[df.columns[0:48]]
            df.to_excel(Carpeta_archivos_guardar + r"\MOD_ANDALUCÍA_Sevilla.xlsx", index=True)
            print ('BBDD Andalucía (Sevilla) creada') 
            informe = pd.DataFrame({'Comunidad autónoma':['Andalucía (Sevilla)'], 'Total de certificados':[duplicados], 'Total de certificados correctos':[df.shape[0]], 'Certificados eliminados por estar duplicados':[duplicados - df.shape[0]]})
            informe_CCAA = pd.concat([informe_CCAA, informe], axis=0)
        except:
                print ('No hay datos de Andalucía o alguna provincia') 

    informe_CCAA.to_excel(Carpeta_archivos_guardar + r"\informe_CCAA.xlsx", index=False)



