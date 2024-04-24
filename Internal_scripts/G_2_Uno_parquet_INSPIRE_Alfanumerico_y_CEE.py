# Importante: Recordar hacer el paso G_1_2 antes de este (asigna el tipo de municipio) y de los EPC el paso anterior es el A_9
# Combino los dos catastro con parquet
import pandas as pd
import geopandas as gpd
import numpy as np
from time import time

def combine_cadastres_with_EPCs (cadastres_files, EPC_files, b3_output, B_3_model_name):
            
    # Edificios Unión de España INSPIRE y alfanumérico
    inicio  = time()

    c_Union = (pd.read_parquet(cadastres_files))

    d_CEE = (pd.read_parquet(EPC_files))

    duracion = (time() - inicio)
    print('Ha leido el GIS en ' + str(duracion) + ' segundos')

    print(d_CEE.shape[0])
    num_EPC_original = d_CEE['Numero_de_EPC'].sum()

    # Para que la unión sea un geodataframe debe estar el geodataframe en la pazrte izquierda (left) y en la derecha el dataframe, sino el resultado es un dataframe
    df = pd.merge(c_Union, d_CEE, left_on='reference', right_on='ReferenciaCatastral_edificio')
    print(df.shape[0])
    num_EPC_intermedio = df['Numero_de_EPC'].sum()

    # df['Coincide'] = np.where((df['C_CCAA']== df['ComunAutonoma']), 'Si','No_data')
    # df = df.loc[(df['Coincide'] == 'Si')]
    # df = df.drop(['Coincide'], axis=1)
    # print(df.shape[0])

    # Esto son errores del catastro, son fincas en las que los 7 primeros dígitos son el nº de parcela, los 7 siguientes la hoja de plano y como no tienen (0000000) resulta que coinciden edificios y BI de diferentes zonas de españa con la misma refetencia catastral, como son tan pocos y es tan raro los elimino uno a uno
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00020120000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00010030000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00050060000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00130090000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00070110000000']
    num_EPC_intermedio2 = df['Numero_de_EPC'].sum()

    # Hecho antes, pero por si acaso: Esto son errores del catastro, a veces un Bien Inmueble no tiene Construcciones asociadas dentro y por tanto su superficie es 0 en nuestros cálculos (680 casos aprox.)
    # y también y mucho más frecuente (unos 14000 casos aprox) han certificado bienes inmuebles con elementos constructivos de uso almacén-estacionamiento y estos no puede ser certificados, se eliminan por tanto.
    print(df.shape[0])
    df['Coincide'] = np.where((df['m2_certificados']!= 0), 'Si','Bien')
    df = df.loc[(df['Coincide'] == 'Si')]
    df = df.drop(['Coincide'], axis=1)
    print(str(df.shape[0]) + ' este número debería ser igual al anterior, ya se ha comprobado antes')

    df.to_parquet(b3_output + B_3_model_name + ".gzip", compression='gzip', index=False)
    df.to_csv(b3_output + B_3_model_name + ".csv", index=False)

    duracion_prov = time() - inicio
    print(df.columns)

    num_EPC = df['Numero_de_EPC'].sum()
    num_BI = df['Numero_de_BI_certificados'].sum()
    m2_certif = df['m2_certificados'].sum()

    print('En la unión de catastros con los certificados hay: ' + str(df.shape[0]) + ' edificios\nEn la unión de catastros hay: ' + str(c_Union.shape[0]) + '\nEn los datos de los certificados energéticos con uso hay: ' + str(d_CEE.shape[0]) + '\nY ha tardado: ' + str(duracion_prov) + ' segundos'
        + '\nEn la unión de catastros con los certificados habia originalmente: ' + str(num_EPC_original) + ' y tras la unión (quedan filtros aún): ' + str(num_EPC_intermedio) + ' y tras la comprobar que el EPC esté en la misma CCAA que el edificio y errores catastrales (quedan quitar los edif con sup certif que sea 0): ' + str(num_EPC_intermedio2)
        + '\nEn la unión de catastros con los certificados hay: ' + str(num_EPC) + ' EPC, ' + str(num_BI) + ' Bienes Inmuebles certificados, ' + str(m2_certif) + ' m2 de superficie certificada'
        )

    with open(b3_output + '\\' + r"Datos_National-scale_EPC-based_Building_Energy_Model" + ".txt", 'w') as f:
                        f.write('En la unión de catastros con los certificados hay: ' + str(df.shape[0]) + ' edificios\nEn la unión de catastros hay: ' + str(c_Union.shape[0]) + '\nEn los datos de los certificados energéticos hay: ' + str(d_CEE.shape[0]) + '\nY ha tardado: ' + str(duracion_prov) + ' segundos' 
                                + '\nEn la unión de catastros con los certificados habia originalmente: ' + str(num_EPC_original) + ' y tras la unión (quedan filtros aún): ' + str(num_EPC_intermedio) + ' y tras la comprobar que el EPC esté en la misma CCAA que el edificio y errores catastrales (quedan quitar los edif con sup certif que sea 0): ' + str(num_EPC_intermedio2)
                                + '\nEn la unión de catastros con los certificados hay: ' + str(num_EPC) + ' EPC, ' + str(num_BI) + ' Bienes Inmuebles certificados, ' + str(m2_certif) + ' m2 de superficie certificada'
                                )

    print ('Terminado')

def combine_cadastres_with_EPCs_GIS (cadastres_files, EPC_files, b3_output, B_3_model_name):
            
    # Edificios Unión de España INSPIRE y alfanumérico
    inicio  = time()

    c_Union = (gpd.read_parquet(cadastres_files))

    d_CEE = (pd.read_parquet(EPC_files))

    duracion = (time() - inicio)
    print('Ha leido el GIS en ' + str(duracion) + ' segundos')

    print(d_CEE.shape[0])
    num_EPC_original = d_CEE['Numero_de_EPC'].sum()

    # Para que la unión sea un geodataframe debe estar el geodataframe en la pazrte izquierda (left) y en la derecha el dataframe, sino el resultado es un dataframe
    df = pd.merge(c_Union, d_CEE, left_on='reference', right_on='ReferenciaCatastral_edificio')
    print(df.shape[0])
    num_EPC_intermedio = df['Numero_de_EPC'].sum()

    # df['Coincide'] = np.where((df['C_CCAA']== df['ComunAutonoma']), 'Si','No_data')
    # df = df.loc[(df['Coincide'] == 'Si')]
    # df = df.drop(['Coincide'], axis=1)
    # print(df.shape[0])

    # Esto son errores del catastro, son fincas en las que los 7 primeros dígitos son el nº de parcela, los 7 siguientes la hoja de plano y como no tienen (0000000) resulta que coinciden edificios y BI de diferentes zonas de españa con la misma refetencia catastral, como son tan pocos y es tan raro los elimino uno a uno
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00020120000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00010030000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00050060000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00130090000000']
    df = df.loc[df.loc[:, 'ReferenciaCatastral_edificio'] != '00070110000000']
    num_EPC_intermedio2 = df['Numero_de_EPC'].sum()

    # Hecho antes, pero por si acaso: Esto son errores del catastro, a veces un Bien Inmueble no tiene Construcciones asociadas dentro y por tanto su superficie es 0 en nuestros cálculos (680 casos aprox.)
    # y también y mucho más frecuente (unos 14000 casos aprox) han certificado bienes inmuebles con elementos constructivos de uso almacén-estacionamiento y estos no puede ser certificados, se eliminan por tanto.
    print(df.shape[0])
    df['Coincide'] = np.where((df['m2_certificados']!= 0), 'Si','Bien')
    df = df.loc[(df['Coincide'] == 'Si')]
    df = df.drop(['Coincide'], axis=1)
    print(str(df.shape[0]) + ' este número debería ser igual al anterior, ya se ha comprobado antes')

    df.to_parquet(b3_output + B_3_model_name + ".parquet") 
    df.to_csv(b3_output + B_3_model_name + ".csv", index=False)

    duracion_prov = time() - inicio
    print('Ha hecho el paso B.3 en GIS en ' + str(duracion_prov) + ' segundos')


    print ('Terminado')
