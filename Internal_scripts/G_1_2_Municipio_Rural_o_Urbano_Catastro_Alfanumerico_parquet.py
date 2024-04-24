# Este script es para coger la población de cada municipio según el INE (actualmente a fecha del 1/1/2022), asignarle a cada municipio si es rural o urbano 
# y luego a cada edificio de la unión entre el catastro alfanumérico y el INSPIRE el tipo de municipio en que se encuentra. (Se puede hacer también sólo con el catastro alfanumérico)

import pandas as pd
import numpy as np
from time import time

def assign_type_of_municipality (population_census, Alphanumeric_buildings):

    inicio  = time()
    # Los datos del INE de población por municipios de toda España (https://www.ine.es/dynt3/inebase/es/index.htm?padre=525), del zip me quedo con el más reciente pobmun22
    dtype_dict = {'CPRO': 'str', 'CMUN': 'str'}
    df = (pd.read_excel(population_census, skiprows=1, dtype=dtype_dict))
    # Me salto la primera fila que es encabezado


    # Clasifico en rural o urbano, como hicimos en RuralRegen separo por rural menor a 20000 hab. y urbano de 20001 para arriba
    # Habrá que actualizar el nomnre de la columna conforme pasen los años

    #print(df.shape[0])

    rural = df.loc[df.loc[:, 'POB22'] < 20001]
    urbano = df.loc[df.loc[:, 'POB22'] >= 20001]
    rural.insert(1, 'Tipo_Mun', 'Rural')
    urbano.insert(1, 'Tipo_Mun', 'Urbano')

    municip = pd.concat([rural,urbano], axis=0)
    #municip = municip.drop(['NOMBRE', 'POB22', 'HOMBRES', 'MUJERES'], axis=1)
    #print(municip.shape[0])
    #print(municip)

    df = (pd.read_parquet(Alphanumeric_buildings))
    print(df.shape[0])
    # Para hacer la unión para darle a los edificios del catastro alfanumérico los datos de si el municipio en que está el edificio es rural o urbano hay que hacer coincidir
    # los valores de CPRO y CMUN que da el INE con los valores Provincia y CMunicipioINE del catastro alfanumérico.

    df = pd.merge(df, municip[['CPRO', 'CMUN', 'Tipo_Mun']], how="left", left_on=['Provincia', 'CMunicipioINE'], right_on=['CPRO', 'CMUN'])

    df = df.drop(['CPRO', 'CMUN'], axis=1)
    print (df)
    print (df.columns)
    print(df.shape[0])
    # Sobreescribirá el archivo parquet de la unión de los catastros alfanumérico e INSPIRE con la misma información más el tipo de municipio
    df.to_parquet(Alphanumeric_buildings, compression='gzip', index=False)  

    # df[0:100000].to_csv(Carpeta_archivos_guardar + nombre[0] + '_PruebaPoblación_Reducido' + ".csv", index=False)

    duracion_prov = time() - inicio
    print ('Ha tardado ' + str(duracion_prov) + ' segundos')

    print ('Terminado')



    # NOTAS E INFORMACIÓN INTERESANTE

    # diccionario23 es la relación de los municipios con sus códigos del INE a feha 1/1/2023 lo que nos permite asignarle el nombre oficial del municipio, datos sobre población y así
    # https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177031&menu=ultiDatos&idp=1254734710990


    # La población por municipio, nos permitiría categorizarlo por rural y urbano, rural grande, pequeño...
    # Es el zip pobmun, y el primer archivo, pobmun22 son los datos de toda España municipio a municipio a fecha del 2022.
    # https://www.ine.es/dynt3/inebase/es/index.htm?padre=525


    # En el INE también está la información de % de hombres y mujeres por municipio y así que se podría integrar también.
    # https://www.ine.es/dynt3/inebase/es/index.htm?padre=525



