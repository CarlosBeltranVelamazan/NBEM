# Importante: Antes de este paso va del alfanumérico: el E_script_clave, el D_7_Convierte_csv_a_parquet y el D_9_Catastro_Alfanumerico_parquet_Quito_columnas_inutiles
# Combino los dos catastro con parquet

import pandas as pd
import geopandas as gpd
import numpy as np
from time import time

def combine_cadastres (INSPIRE_buildings, Alphanumeric_buildings, b2_output, B_2_model_name):

        # Edificios de España INSPIRE
        inicio  = time()
        c_INSPIRE = INSPIRE_buildings

        # Edificios de España catastro ALFANUMERICO
        c_alfanum = Alphanumeric_buildings

        Carpeta_archivos_guardar = b2_output

        # Lee los catastros (como datos tabulares)
        c_INSPIRE = (pd.read_parquet(c_INSPIRE))

        c_alfanum = (pd.read_parquet(c_alfanum))

        duracion = (time() - inicio)
        print('Ha leido el GIS en ' + str(duracion) + ' segundos')

        print(c_alfanum.shape[0])
        print(c_alfanum.dtypes)
        print(c_INSPIRE.dtypes)

        # Este código en teoría no es necesario, sin embargo si que sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino muchos errores
        pre_borrar = c_INSPIRE.shape[0]
        c_INSPIRE = c_INSPIRE.drop_duplicates(subset=['reference'], keep=False)
        duplicados = c_INSPIRE.shape[0] - pre_borrar
        if duplicados != 0:
                print ('Se han borrado por duplicados ' + str(duplicados) + ' referencias catastrales en el Cat INSPIRE')


        # Este código en teoría no es necesario, sin embargo si que sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino muchos errores
        pre_borrar = c_alfanum.shape[0]
        c_alfanum = c_alfanum.drop_duplicates(subset=['ReferenciaCatastral_parcela'], keep=False)
        duplicados = c_alfanum.shape[0] - pre_borrar
        if duplicados != 0:
                print ('Se han borrado por duplicados ' + str(duplicados) + ' referencias catastrales en el Cat Alfanumérico')

        # Para que la unión sea un geodataframe debe estar el geodataframe en la pazrte izquierda (left) y en la derecha el dataframe, sino el resultado es un dataframe

        df = pd.merge(c_INSPIRE, c_alfanum, left_on='reference', right_on='ReferenciaCatastral_parcela')
        print('En la unión de catastros hay: ' + str(df.shape[0]) + ' en el alfanumerico: ' + str(c_alfanum.shape[0]) + ' en el INSPIRE: ' + str(c_INSPIRE.shape[0]))


        # Para agrupar por Comunidad autonoma le añado esta columna:
        # df.insert(1, 'ComunAutonoma', df.Provincia) 
        # df.ComunAutonoma.replace ({'04':1, '11':1, '14':1, '18':1, '21':1, '23':1, '29':1, '41':1,
        #                         '22':2, '44':2, '50':2, '33':3, '07':4, '35':5, '38':5, '39':6,
        #                         '05':7, '09':7, '24':7, '34':7, '37':7, '40':7, '42':7, '47':7, '49':7,
        #                         '02':8, '13':8, '16':8, '19':8, '45':8, 
        #                         '08':9, '17':9, '25':9, '43':9, '03':10, '12':10, '46':10, 
        #                         '06':11, '10':11, '15':12, '27':12, '32':12, '36':12, 
        #                         '28':13, '30':14, '31':15, '01':16, '48':16, '20':16,
        #                         '26':17, '51':18, '52':19
        #                         }, inplace=True)

        # Para agrupar por los datos de la EPBD, público (residencial y no residencial), residencial y no residencial:       # IMPORTANTE: El catastro INSPIRE da Uso Público, no propiedad Pública
        df['Cluster_EPBD'] = np.where((df['Viv'] >=1), 'Residencial',
                        np.where((df['Viv'] <1), 'No Residencial','No_data'
                                        ))
        # Para agrupar por los datos de la EPBD, público (residencial y no residencial), residencial y no residencial:       # IMPORTANTE: El catastro INSPIRE da Uso Público, no propiedad Pública
        # df['Cluster_EPBD'] = np.where((df['currentUse']== '4_3_publicServices'), 'Público',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] >=1), 'Residencial',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] <1), 'No Residencial','No_data'
        #                                      )))

        # Para agrupar por los datos de la EPBD separando en residencial público y privado:      # IMPORTANTE: el catastro INSPIRE da Uso Público, no propiedad Pública
        # df['Cluster_EPBD'] = np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] >=1), 'Público residencial',
        #                      np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] <1), 'Público no residencial',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] >=1), 'Residencial',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] <1), 'No Residencial','No_data'
        #                                      ))))

        # Para agrupar por los datos de la EPBD con perdiodo de construcción:
        # df['Cluster_EPBD'] = np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] >=1), 'Público residencial ' + df['Periodo_Construccion'],
        #                      np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] <1), 'Público no residencial ' + df['Periodo_Construccion'],
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] >=1), 'Residencial ' + df['Periodo_Construccion'],
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] <1), 'No Residencial ' + df['Periodo_Construccion'],'No_data'
        #                                      ))))
        #print(str(df.shape[0]) + ' antes de la unión final')

        # df = df.groupby('ReferenciaCatastral_parcela').agg(
        #                             ReferenciaCatastral_edificio = ('ReferenciaCatastral_parcela', 'first'))
        # print(str(df.shape[0]) + ' tras la unión final poner el que se guarde si esto está bien')


        # Guardo el resultado en formato parquet
        df.to_parquet(Carpeta_archivos_guardar + B_2_model_name + ".gzip", compression='gzip', index=False)

        num_BI = df['N_BI'].sum()
        num_Viv = df['Viv'].sum()

        duracion_prov = time() - inicio
        with open(Carpeta_archivos_guardar + '\\' + r"Datos_Union_of_cadastres" + ".txt", 'w') as f:
                        f.write('En la unión de catastros hay: ' + str(df.shape[0]) + '\nEn el alfanumerico: ' + str(c_alfanum.shape[0]) + '\nEn el INSPIRE: ' + str(c_INSPIRE.shape[0]) + '\nY ha tardado: ' + str(duracion_prov) + ' segundos' 
                                + '\nEn la unión hay: ' + str(num_BI) + ' bienes inmuebles, de los cuáles '+ str(num_Viv) + ' son viviendas'
                                )

        print ('Terminado')


def combine_cadastres_GIS (INSPIRE_buildings, Alphanumeric_buildings, b2_output, B_2_model_name):

        # Edificios de España INSPIRE
        inicio  = time()
        c_INSPIRE = INSPIRE_buildings

        # Edificios de España catastro ALFANUMERICO
        c_alfanum = Alphanumeric_buildings

        Carpeta_archivos_guardar = b2_output

        # Lee los catastros
        #columns_to_use = ['reference', 'beginning', 'conditionOfConstruction', 'currentUse', 'numberOfBuildingUnits', 'numberOfDwellings', 'value', 'geometry']
        #c_INSPIRE = (gpd.read_parquet(c_INSPIRE, columns=columns_to_use))
        c_INSPIRE = (gpd.read_parquet(c_INSPIRE))
        c_alfanum = (pd.read_parquet(c_alfanum))

        duracion = (time() - inicio)
        print('Ha leido el GIS en ' + str(duracion) + ' segundos')

        print(c_alfanum.shape[0])
        print(c_alfanum.dtypes)
        print(c_INSPIRE.dtypes)

        # Este código en teoría no es necesario, sin embargo si que sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino muchos errores
        pre_borrar = c_INSPIRE.shape[0]
        c_INSPIRE = c_INSPIRE.drop_duplicates(subset=['reference'], keep=False)
        duplicados = c_INSPIRE.shape[0] - pre_borrar
        if duplicados != 0:
                print ('Se han borrado por duplicados ' + str(duplicados) + ' referencias catastrales en el Cat INSPIRE')

        # Este código en teoría no es necesario, sin embargo si que sucede que hay referencias catastrales que van a 2 edificios diferentes, opto por agrupar y que se quede en un único edificio y fin, así elimino muchos errores
        pre_borrar = c_alfanum.shape[0]
        c_alfanum = c_alfanum.drop_duplicates(subset=['ReferenciaCatastral_parcela'], keep=False)
        duplicados = c_alfanum.shape[0] - pre_borrar
        if duplicados != 0:
                print ('Se han borrado por duplicados ' + str(duplicados) + ' referencias catastrales en el Cat Alfanumérico')

        # Para que la unión sea un geodataframe debe estar el geodataframe en la pazrte izquierda (left) y en la derecha el dataframe, sino el resultado es un dataframe

        df = pd.merge(c_INSPIRE, c_alfanum, left_on='reference', right_on='ReferenciaCatastral_parcela')
        print('En la unión de catastros hay: ' + str(df.shape[0]) + ' en el alfanumerico: ' + str(c_alfanum.shape[0]) + ' en el INSPIRE: ' + str(c_INSPIRE.shape[0]))


        # Para agrupar por Comunidad autonoma le añado esta columna:
        # df.insert(1, 'ComunAutonoma', df.Provincia) 
        # df.ComunAutonoma.replace ({'04':1, '11':1, '14':1, '18':1, '21':1, '23':1, '29':1, '41':1,
        #                         '22':2, '44':2, '50':2, '33':3, '07':4, '35':5, '38':5, '39':6,
        #                         '05':7, '09':7, '24':7, '34':7, '37':7, '40':7, '42':7, '47':7, '49':7,
        #                         '02':8, '13':8, '16':8, '19':8, '45':8, 
        #                         '08':9, '17':9, '25':9, '43':9, '03':10, '12':10, '46':10, 
        #                         '06':11, '10':11, '15':12, '27':12, '32':12, '36':12, 
        #                         '28':13, '30':14, '31':15, '01':16, '48':16, '20':16,
        #                         '26':17, '51':18, '52':19
        #                         }, inplace=True)

        # Para agrupar por los datos de la EPBD, público (residencial y no residencial), residencial y no residencial:       # IMPORTANTE: El catastro INSPIRE da Uso Público, no propiedad Pública
        df['Cluster_EPBD'] = np.where((df['Viv'] >=1), 'Residencial',
                        np.where((df['Viv'] <1), 'No Residencial','No_data'
                                        ))
        # Para agrupar por los datos de la EPBD, público (residencial y no residencial), residencial y no residencial:       # IMPORTANTE: El catastro INSPIRE da Uso Público, no propiedad Pública
        # df['Cluster_EPBD'] = np.where((df['currentUse']== '4_3_publicServices'), 'Público',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] >=1), 'Residencial',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] <1), 'No Residencial','No_data'
        #                                      )))

        # Para agrupar por los datos de la EPBD separando en residencial público y privado:      # IMPORTANTE: el catastro INSPIRE da Uso Público, no propiedad Pública
        # df['Cluster_EPBD'] = np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] >=1), 'Público residencial',
        #                      np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] <1), 'Público no residencial',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] >=1), 'Residencial',
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] <1), 'No Residencial','No_data'
        #                                      ))))

        # Para agrupar por los datos de la EPBD con perdiodo de construcción:
        # df['Cluster_EPBD'] = np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] >=1), 'Público residencial ' + df['Periodo_Construccion'],
        #                      np.where((df['currentUse']== '4_3_publicServices') & (df['Viv'] <1), 'Público no residencial ' + df['Periodo_Construccion'],
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] >=1), 'Residencial ' + df['Periodo_Construccion'],
        #                      np.where((df['currentUse']!= '4_3_publicServices') & (df['Viv'] <1), 'No Residencial ' + df['Periodo_Construccion'],'No_data'
        #                                      ))))
        #print(str(df.shape[0]) + ' antes de la unión final')

        # df = df.groupby('ReferenciaCatastral_parcela').agg(
        #                             ReferenciaCatastral_edificio = ('ReferenciaCatastral_parcela', 'first'))
        # print(str(df.shape[0]) + ' tras la unión final poner el que se guarde si esto está bien')

        # Guardo el resultado en formato parquet
        df.to_parquet(Carpeta_archivos_guardar + B_2_model_name + ".parquet") 

        print ('Terminado')
