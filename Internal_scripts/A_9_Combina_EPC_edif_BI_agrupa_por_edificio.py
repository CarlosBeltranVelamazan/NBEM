def group_by_building (b1_14_digits, b1_20_digits, b1_output, B_1_model_name):

    import pandas as pd
    import numpy as np
    from simpledbf import Dbf5
    from time import time
    inicio  = time()

    # La BBDD de los certificados energéticos separados en CEE de 20 dígitos (edificios) y de 14 (Bienes inmuebles)
    #Certificados_uso = 0    # En este paso separamos por uso según catastro, aquí hay que poner este valor a 0 siempre

    # Columnas que queremos conservar en el df, las que no estén aquí se borrarán
    colsusar = ['Uso_certificado', 'Numero_de_BI_certificados', 'm2_certificados',
        'ReferenciaCatastral_edificio', 'Consumo_energia_primaria_medio', 'Consumo_energia_primaria_mediano',
        'Emisiones_CO2_medio', 'Emisiones_CO2_mediano', 'Numero_de_EPC', 
        'A_EP', 'B_EP', 'C_EP', 'D_EP', 'E_EP', 'F_EP', 'G_EP', 
        'A_CO2', 'B_CO2', 'C_CO2', 'D_CO2', 'E_CO2', 'F_CO2', 'G_CO2', 
        'A_EP_m2', 'B_EP_m2', 'C_EP_m2', 'D_EP_m2', 'E_EP_m2', 'F_EP_m2', 'G_EP_m2', 
        'A_CO2_m2', 'B_CO2_m2', 'C_CO2_m2', 'D_CO2_m2', 'E_CO2_m2', 'F_CO2_m2', 'G_CO2_m2', 
        'A_EP_BI', 'B_EP_BI', 'C_EP_BI', 'D_EP_BI', 'E_EP_BI', 'F_EP_BI', 'G_EP_BI', 
        'A_CO2_BI', 'B_CO2_BI', 'C_CO2_BI', 'D_CO2_BI', 'E_CO2_BI', 'F_CO2_BI', 'G_CO2_BI', 
        'C_CCAA', 'CPROV', 'TipoEdificio', 'Fecha_registro',]

    # Archivo con los EPC de edificios
    df14 = b1_14_digits
    df14 = df14[df14.columns.intersection(colsusar)]

    # Archivo con los EPC de bienes inmuebles
    df20 = b1_20_digits
    df20 = df20[df20.columns.intersection(colsusar)]


    # Para poder sacar el valor del consumo de energía y de emisiones ponderado por superficie
    df14.insert(1, 'Consumo_energia_primaria_medio_sup', df14['m2_certificados']*df14['Consumo_energia_primaria_medio'])
    df14.insert(2, 'Consumo_energia_primaria_mediano_sup', df14['m2_certificados']*df14['Consumo_energia_primaria_mediano'])
    df14.insert(3, 'Emisiones_CO2_medio_sup', df14['m2_certificados']*df14['Emisiones_CO2_medio'])
    df14.insert(4, 'Emisiones_CO2_mediano_sup', df14['m2_certificados']*df14['Emisiones_CO2_mediano'])
    df20.insert(1, 'Consumo_energia_primaria_medio_sup', df20['m2_certificados']*df20['Consumo_energia_primaria_medio'])
    df20.insert(2, 'Consumo_energia_primaria_mediano_sup', df20['m2_certificados']*df20['Consumo_energia_primaria_mediano'])
    df20.insert(3, 'Emisiones_CO2_medio_sup', df20['m2_certificados']*df20['Emisiones_CO2_medio'])
    df20.insert(4, 'Emisiones_CO2_mediano_sup', df20['m2_certificados']*df20['Emisiones_CO2_mediano'])

    # Numero de EPC antes de la unión
    a = df14.shape[0]
    b = df20.shape[0]

    pre_borrar = df14.shape[0]
    df14 ['m2_certificados'] = df14['m2_certificados']. fillna('None')
    df14['Coincide'] = np.where((df14['m2_certificados']!= 'None'), 'Si','Bien')
    df14 = df14.loc[(df14['Coincide'] == 'Si')]
    df14['Coincide'] = np.where((df14['m2_certificados']!= 0), 'Si','Bien')
    df14 = df14.loc[(df14['Coincide'] == 'Si')]
    df14 = df14.drop(['Coincide'], axis=1)
    duplicados = df14.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' df14')

    pre_borrar = df20.shape[0]
    df20 ['m2_certificados'] = df20['m2_certificados']. fillna('None')
    df20['Coincide'] = np.where((df20['m2_certificados']!= 'None'), 'Si','Bien')
    df20 = df20.loc[(df20['Coincide'] == 'Si')]
    df20['Coincide'] = np.where((df20['m2_certificados']!= 0), 'Si','Bien')
    df20 = df20.loc[(df20['Coincide'] == 'Si')]
    df20 = df20.drop(['Coincide'], axis=1)
    duplicados = df20.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' df20')


    # La BBDD de EPC combinando ambas
    GranBBDD = pd.DataFrame()
    GranBBDD = pd.concat([GranBBDD, df14, df20], axis=0)
    c = GranBBDD.shape[0]


    pre_borrar = GranBBDD.shape[0]
    GranBBDD['Coincide'] = np.where((GranBBDD['m2_certificados']!= 0), 'Si','Bien')
    mal = GranBBDD.loc[(GranBBDD['Coincide'] == 'Bien')]
    GranBBDD = GranBBDD.loc[(GranBBDD['Coincide'] == 'Si')]
    GranBBDD = GranBBDD.drop(['Coincide'], axis=1)
    duplicados = GranBBDD.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' edif3333')

    pre_borrar = GranBBDD.shape[0]
    GranBBDD['m2_certificados'] = GranBBDD['m2_certificados']. fillna('None')
    GranBBDD['Coincide'] = np.where((GranBBDD['m2_certificados']!= 'None'), 'Si','Bien')
    GranBBDD = GranBBDD.loc[(GranBBDD['Coincide'] == 'Si')]
    GranBBDD = GranBBDD.drop(['Coincide'], axis=1)
    duplicados = GranBBDD.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' edif4444')



    GranBBDD_resid1 = GranBBDD.loc[GranBBDD.loc[:, 'Uso_certificado'] == 'Residencial - Bloque completo o unifamiliar']
    GranBBDD_resid2 = GranBBDD.loc[GranBBDD.loc[:, 'Uso_certificado'] == 'Residencial - Vivienda invidual o unifamiliar']
    GranBBDD_resid = pd.concat([GranBBDD_resid1, GranBBDD_resid2], axis=0)

    GranBBDD_terc1 = GranBBDD.loc[GranBBDD.loc[:, 'Uso_certificado'] == 'Terciario - Edificio completo']
    GranBBDD_terc2 = GranBBDD.loc[GranBBDD.loc[:, 'Uso_certificado'] == 'Terciario - Local']
    GranBBDD_terc = pd.concat([GranBBDD_terc1, GranBBDD_terc2], axis=0)

    d = GranBBDD_resid.shape[0]
    e = GranBBDD_terc.shape[0]

    GranBBDD = GranBBDD.groupby('ReferenciaCatastral_edificio').agg(
                                ReferenciaCatastral_edificio = ('ReferenciaCatastral_edificio', 'first'), \
                                Consumo_energia_primaria_medio = ('Consumo_energia_primaria_medio', 'mean'), \
                                Consumo_energia_primaria_mediano = ('Consumo_energia_primaria_mediano', 'median'), \
                                Consumo_energia_primaria_medio_sup = ('Consumo_energia_primaria_medio_sup', 'sum'), \
                                Consumo_energia_primaria_mediano_sup = ('Consumo_energia_primaria_mediano_sup', 'sum'), \
                                Emisiones_CO2_medio = ('Emisiones_CO2_medio', 'mean'), \
                                Emisiones_CO2_mediano = ('Emisiones_CO2_mediano', 'median'), \
                                Emisiones_CO2_medio_sup = ('Emisiones_CO2_medio_sup', 'sum'), \
                                Emisiones_CO2_mediano_sup = ('Emisiones_CO2_mediano_sup', 'sum'), \
                                C_CCAA = ('C_CCAA', 'first'), \
                                CPROV = ('CPROV', 'first'), \
                                Numero_de_EPC = ('Numero_de_EPC', 'sum'), \
                                Numero_de_BI_certificados = ('Numero_de_BI_certificados', 'sum'), \
                                m2_certificados = ('m2_certificados', 'sum'), \
                                A_EP = ('A_EP', 'sum'), \
                                B_EP = ('B_EP', 'sum'), \
                                C_EP = ('C_EP', 'sum'), \
                                D_EP = ('D_EP', 'sum'), \
                                E_EP = ('E_EP', 'sum'), \
                                F_EP = ('F_EP', 'sum'), \
                                G_EP = ('G_EP', 'sum'), \
                                A_CO2 = ('A_CO2', 'sum'), \
                                B_CO2 = ('B_CO2', 'sum'), \
                                C_CO2 = ('C_CO2', 'sum'), \
                                D_CO2 = ('D_CO2', 'sum'), \
                                E_CO2 = ('E_CO2', 'sum'), \
                                F_CO2 = ('F_CO2', 'sum'), \
                                G_CO2 = ('G_CO2', 'sum'), \
                                A_EP_m2 = ('A_EP_m2', 'sum'), \
                                B_EP_m2 = ('B_EP_m2', 'sum'), \
                                C_EP_m2 = ('C_EP_m2', 'sum'), \
                                D_EP_m2 = ('D_EP_m2', 'sum'), \
                                E_EP_m2 = ('E_EP_m2', 'sum'), \
                                F_EP_m2 = ('F_EP_m2', 'sum'), \
                                G_EP_m2 = ('G_EP_m2', 'sum'), \
                                A_CO2_m2 = ('A_CO2_m2', 'sum'), \
                                B_CO2_m2 = ('B_CO2_m2', 'sum'), \
                                C_CO2_m2 = ('C_CO2_m2', 'sum'), \
                                D_CO2_m2 = ('D_CO2_m2', 'sum'), \
                                E_CO2_m2 = ('E_CO2_m2', 'sum'), \
                                F_CO2_m2 = ('F_CO2_m2', 'sum'), \
                                G_CO2_m2 = ('G_CO2_m2', 'sum'), \
                                A_EP_BI = ('A_EP_BI', 'sum'), \
                                B_EP_BI = ('B_EP_BI', 'sum'), \
                                C_EP_BI = ('C_EP_BI', 'sum'), \
                                D_EP_BI = ('D_EP_BI', 'sum'), \
                                E_EP_BI = ('E_EP_BI', 'sum'), \
                                F_EP_BI = ('F_EP_BI', 'sum'), \
                                G_EP_BI = ('G_EP_BI', 'sum'), \
                                A_CO2_BI = ('A_CO2_BI', 'sum'), \
                                B_CO2_BI = ('B_CO2_BI', 'sum'), \
                                C_CO2_BI = ('C_CO2_BI', 'sum'), \
                                D_CO2_BI = ('D_CO2_BI', 'sum'), \
                                E_CO2_BI = ('E_CO2_BI', 'sum'), \
                                F_CO2_BI = ('F_CO2_BI', 'sum'), \
                                G_CO2_BI = ('G_CO2_BI', 'sum'), \
                                    )    
    w = GranBBDD.shape[0]

    num_EPC_todos_prov = GranBBDD['Numero_de_EPC'].sum()
    # Al hacer la unión de EPC por edificio, si había de edificio completo y de BI individual se han sumado el Nº de BI y los m2 certificados y hay más de que en edificio en si
    # Con este código le doy los valores de Nº de BI y los m2 certificados del EPC del edificio entero. Agrupo todos los EPC de edificio (para dejar las columnas y todo iguales, ya no debería haber EPC duplicados ni en la misma BBDD que se quita en el paso A1 ni que esté el mismo edificio en 2 BBDD diferentes que se quita en el A_8)
    print ('Datos para ver que esté bien: ')
    print (df14.shape[0])
    df14_agrup = df14.groupby('ReferenciaCatastral_edificio').agg(
                                ReferenciaCatastral_edificio = ('ReferenciaCatastral_edificio', 'first'), \
                                Consumo_energia_primaria_medio = ('Consumo_energia_primaria_medio', 'mean'), \
                                Consumo_energia_primaria_mediano = ('Consumo_energia_primaria_mediano', 'median'), \
                                Consumo_energia_primaria_medio_sup = ('Consumo_energia_primaria_medio_sup', 'sum'), \
                                Consumo_energia_primaria_mediano_sup = ('Consumo_energia_primaria_mediano_sup', 'sum'), \
                                Emisiones_CO2_medio = ('Emisiones_CO2_medio', 'mean'), \
                                Emisiones_CO2_mediano = ('Emisiones_CO2_mediano', 'median'), \
                                Emisiones_CO2_medio_sup = ('Emisiones_CO2_medio_sup', 'sum'), \
                                Emisiones_CO2_mediano_sup = ('Emisiones_CO2_mediano_sup', 'sum'), \
                                C_CCAA = ('C_CCAA', 'first'), \
                                CPROV = ('CPROV', 'first'), \
                                Numero_de_EPC = ('Numero_de_EPC', 'sum'), \
                                Numero_de_BI_certificados = ('Numero_de_BI_certificados', 'sum'), \
                                m2_certificados = ('m2_certificados', 'sum'), \
                                A_EP = ('A_EP', 'sum'), \
                                B_EP = ('B_EP', 'sum'), \
                                C_EP = ('C_EP', 'sum'), \
                                D_EP = ('D_EP', 'sum'), \
                                E_EP = ('E_EP', 'sum'), \
                                F_EP = ('F_EP', 'sum'), \
                                G_EP = ('G_EP', 'sum'), \
                                A_CO2 = ('A_CO2', 'sum'), \
                                B_CO2 = ('B_CO2', 'sum'), \
                                C_CO2 = ('C_CO2', 'sum'), \
                                D_CO2 = ('D_CO2', 'sum'), \
                                E_CO2 = ('E_CO2', 'sum'), \
                                F_CO2 = ('F_CO2', 'sum'), \
                                G_CO2 = ('G_CO2', 'sum'), \
                                A_EP_m2 = ('A_EP_m2', 'sum'), \
                                B_EP_m2 = ('B_EP_m2', 'sum'), \
                                C_EP_m2 = ('C_EP_m2', 'sum'), \
                                D_EP_m2 = ('D_EP_m2', 'sum'), \
                                E_EP_m2 = ('E_EP_m2', 'sum'), \
                                F_EP_m2 = ('F_EP_m2', 'sum'), \
                                G_EP_m2 = ('G_EP_m2', 'sum'), \
                                A_CO2_m2 = ('A_CO2_m2', 'sum'), \
                                B_CO2_m2 = ('B_CO2_m2', 'sum'), \
                                C_CO2_m2 = ('C_CO2_m2', 'sum'), \
                                D_CO2_m2 = ('D_CO2_m2', 'sum'), \
                                E_CO2_m2 = ('E_CO2_m2', 'sum'), \
                                F_CO2_m2 = ('F_CO2_m2', 'sum'), \
                                G_CO2_m2 = ('G_CO2_m2', 'sum'), \
                                A_EP_BI = ('A_EP_BI', 'sum'), \
                                B_EP_BI = ('B_EP_BI', 'sum'), \
                                C_EP_BI = ('C_EP_BI', 'sum'), \
                                D_EP_BI = ('D_EP_BI', 'sum'), \
                                E_EP_BI = ('E_EP_BI', 'sum'), \
                                F_EP_BI = ('F_EP_BI', 'sum'), \
                                G_EP_BI = ('G_EP_BI', 'sum'), \
                                A_CO2_BI = ('A_CO2_BI', 'sum'), \
                                B_CO2_BI = ('B_CO2_BI', 'sum'), \
                                C_CO2_BI = ('C_CO2_BI', 'sum'), \
                                D_CO2_BI = ('D_CO2_BI', 'sum'), \
                                E_CO2_BI = ('E_CO2_BI', 'sum'), \
                                F_CO2_BI = ('F_CO2_BI', 'sum'), \
                                G_CO2_BI = ('G_CO2_BI', 'sum'), \
                                )   
    print (df14_agrup.shape[0])

    df14_agrup.reset_index(drop = True, inplace = True)
    GranBBDD.reset_index(drop = True, inplace = True)

    # Al hacer esta unión elimino los EPC que tienen un certificado de edificio, luego las uniré con los EPC de edificios de nuevo que tendrán los Nº de BI y de m2 certificados bien, los del edificio
    print ('La BBDD total tenia y tiene: ')
    print (GranBBDD.shape[0])

    concatenation = pd.DataFrame()
    concatenation = pd.concat([
                concatenation,
                GranBBDD[GranBBDD['ReferenciaCatastral_edificio'].isin(df14_agrup['ReferenciaCatastral_edificio']) == False],
                ])

    GranBBDD = concatenation
    print (GranBBDD.shape[0])

    GranBBDD = pd.concat([GranBBDD, df14_agrup], axis=0)
    print (GranBBDD.shape[0])

    num_EPC_todos = GranBBDD['Numero_de_EPC'].sum()

    # Para poder sacar el valor del consumo de energía y de emisiones ponderado por superficie, lo cmambio por el que estaba sin ponderar en este punto,
    # así si quiero hacer cualquier comprobación comparando valores puedo hacerlo solamente poniendo un _sup a las variables y quitando el drop y me salen ambos datos por edificio
    # El mediano ahora mismo no lo estoy sacando, no hago la mediana en ningún momento, lo dejo por si sirve para más adelante
    GranBBDD.Consumo_energia_primaria_medio = GranBBDD.Consumo_energia_primaria_medio_sup / GranBBDD.m2_certificados
    # GranBBDD.Consumo_energia_primaria_mediano = GranBBDD.Consumo_energia_primaria_mediano_sup / GranBBDD.m2_certificados
    GranBBDD.Emisiones_CO2_medio = GranBBDD.Emisiones_CO2_medio_sup / GranBBDD.m2_certificados
    # GranBBDD.Emisiones_CO2_mediano = GranBBDD.Emisiones_CO2_mediano_sup / GranBBDD.m2_certificados

    GranBBDD = GranBBDD.drop(['Consumo_energia_primaria_medio_sup'], axis=1)
    GranBBDD = GranBBDD.drop(['Consumo_energia_primaria_mediano_sup'], axis=1)
    GranBBDD = GranBBDD.drop(['Emisiones_CO2_medio_sup'], axis=1)
    GranBBDD = GranBBDD.drop(['Emisiones_CO2_mediano_sup'], axis=1)
    GranBBDD = GranBBDD.drop(['Consumo_energia_primaria_mediano'], axis=1)
    GranBBDD = GranBBDD.drop(['Emisiones_CO2_mediano'], axis=1)

    # Como Castilla La Mancha no da los datos de Consumo y emisiones, los resultados aquí salen 0 y para las medias nacionales cambiarian los resultados, hay que cambiarlos por None
    GranBBDD.Consumo_energia_primaria_medio.replace ({0:None}, inplace=True)
    GranBBDD.Emisiones_CO2_medio.replace ({0:None}, inplace=True)


    pre_borrar = GranBBDD.shape[0]
    GranBBDD['Coincide'] = np.where((GranBBDD['m2_certificados']!= 0), 'Si','Bien')
    mal = GranBBDD.loc[(GranBBDD['Coincide'] == 'Bien')]
    GranBBDD = GranBBDD.loc[(GranBBDD['Coincide'] == 'Si')]
    GranBBDD = GranBBDD.drop(['Coincide'], axis=1)
    duplicados = GranBBDD.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' edif')

    mal.to_csv(b1_output + r"\EPC_m2_mal" + ".csv", index=False)

    GranBBDD.to_csv(b1_output + B_1_model_name + ".csv", index=False)
    GranBBDD.to_parquet(b1_output + B_1_model_name + ".gzip", compression='gzip', index=False)



    # Datos residenciales
    GranBBDD_resid = GranBBDD_resid.groupby('ReferenciaCatastral_edificio').agg(
                                ReferenciaCatastral_edificio = ('ReferenciaCatastral_edificio', 'first'), \
                                Consumo_energia_primaria_medio = ('Consumo_energia_primaria_medio', 'mean'), \
                                Consumo_energia_primaria_mediano = ('Consumo_energia_primaria_mediano', 'median'), \
                                Consumo_energia_primaria_medio_sup = ('Consumo_energia_primaria_medio_sup', 'sum'), \
                                Consumo_energia_primaria_mediano_sup = ('Consumo_energia_primaria_mediano_sup', 'sum'), \
                                Emisiones_CO2_medio = ('Emisiones_CO2_medio', 'mean'), \
                                Emisiones_CO2_mediano = ('Emisiones_CO2_mediano', 'median'), \
                                Emisiones_CO2_medio_sup = ('Emisiones_CO2_medio_sup', 'sum'), \
                                Emisiones_CO2_mediano_sup = ('Emisiones_CO2_mediano_sup', 'sum'), \
                                C_CCAA = ('C_CCAA', 'first'), \
                                CPROV = ('CPROV', 'first'), \
                                Numero_de_EPC = ('Numero_de_EPC', 'sum'), \
                                Numero_de_BI_certificados = ('Numero_de_BI_certificados', 'sum'), \
                                m2_certificados = ('m2_certificados', 'sum'), \
                                A_EP = ('A_EP', 'sum'), \
                                B_EP = ('B_EP', 'sum'), \
                                C_EP = ('C_EP', 'sum'), \
                                D_EP = ('D_EP', 'sum'), \
                                E_EP = ('E_EP', 'sum'), \
                                F_EP = ('F_EP', 'sum'), \
                                G_EP = ('G_EP', 'sum'), \
                                A_CO2 = ('A_CO2', 'sum'), \
                                B_CO2 = ('B_CO2', 'sum'), \
                                C_CO2 = ('C_CO2', 'sum'), \
                                D_CO2 = ('D_CO2', 'sum'), \
                                E_CO2 = ('E_CO2', 'sum'), \
                                F_CO2 = ('F_CO2', 'sum'), \
                                G_CO2 = ('G_CO2', 'sum'), \
                                A_EP_m2 = ('A_EP_m2', 'sum'), \
                                B_EP_m2 = ('B_EP_m2', 'sum'), \
                                C_EP_m2 = ('C_EP_m2', 'sum'), \
                                D_EP_m2 = ('D_EP_m2', 'sum'), \
                                E_EP_m2 = ('E_EP_m2', 'sum'), \
                                F_EP_m2 = ('F_EP_m2', 'sum'), \
                                G_EP_m2 = ('G_EP_m2', 'sum'), \
                                A_CO2_m2 = ('A_CO2_m2', 'sum'), \
                                B_CO2_m2 = ('B_CO2_m2', 'sum'), \
                                C_CO2_m2 = ('C_CO2_m2', 'sum'), \
                                D_CO2_m2 = ('D_CO2_m2', 'sum'), \
                                E_CO2_m2 = ('E_CO2_m2', 'sum'), \
                                F_CO2_m2 = ('F_CO2_m2', 'sum'), \
                                G_CO2_m2 = ('G_CO2_m2', 'sum'), \
                                A_EP_BI = ('A_EP_BI', 'sum'), \
                                B_EP_BI = ('B_EP_BI', 'sum'), \
                                C_EP_BI = ('C_EP_BI', 'sum'), \
                                D_EP_BI = ('D_EP_BI', 'sum'), \
                                E_EP_BI = ('E_EP_BI', 'sum'), \
                                F_EP_BI = ('F_EP_BI', 'sum'), \
                                G_EP_BI = ('G_EP_BI', 'sum'), \
                                A_CO2_BI = ('A_CO2_BI', 'sum'), \
                                B_CO2_BI = ('B_CO2_BI', 'sum'), \
                                C_CO2_BI = ('C_CO2_BI', 'sum'), \
                                D_CO2_BI = ('D_CO2_BI', 'sum'), \
                                E_CO2_BI = ('E_CO2_BI', 'sum'), \
                                F_CO2_BI = ('F_CO2_BI', 'sum'), \
                                G_CO2_BI = ('G_CO2_BI', 'sum'), \
                                )    
    g = GranBBDD_resid.shape[0]

    pre_borrar = GranBBDD_resid.shape[0]
    GranBBDD_resid['Coincide'] = np.where((GranBBDD_resid['m2_certificados']!= 0), 'Si','Bien')
    GranBBDD_resid = GranBBDD_resid.loc[(GranBBDD_resid['Coincide'] == 'Si')]
    GranBBDD_resid = GranBBDD_resid.drop(['Coincide'], axis=1)
    duplicados = GranBBDD_resid.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' edif resid 22222')


    num_EPC_resid_prov = GranBBDD_resid['Numero_de_EPC'].sum()
    # Al hacer la unión de EPC por edificio, si había de edificio completo y de BI individual se han sumado el Nº de BI y los m2 certificados y hay más de que en edificio en si
    # Con este código le doy los valores de Nº de BI y los m2 certificados del EPC del edificio entero. Agrupo todos los EPC de edificio (para dejar las columnas y todo iguales, ya no debería haber EPC duplicados ni en la misma BBDD que se quita en el paso A1 ni que esté el mismo edificio en 2 BBDD diferentes que se quita en el A_8)
    print ('Datos para ver que esté bien: ')
    df14_resid = df14.loc[df14.loc[:, 'Uso_certificado'] == 'Residencial - Bloque completo o unifamiliar']
    print (df14_resid.shape[0])
    df14_agrup = df14_resid.groupby('ReferenciaCatastral_edificio').agg(
                                ReferenciaCatastral_edificio = ('ReferenciaCatastral_edificio', 'first'), \
                                Consumo_energia_primaria_medio = ('Consumo_energia_primaria_medio', 'mean'), \
                                Consumo_energia_primaria_mediano = ('Consumo_energia_primaria_mediano', 'median'), \
                                Consumo_energia_primaria_medio_sup = ('Consumo_energia_primaria_medio_sup', 'sum'), \
                                Consumo_energia_primaria_mediano_sup = ('Consumo_energia_primaria_mediano_sup', 'sum'), \
                                Emisiones_CO2_medio = ('Emisiones_CO2_medio', 'mean'), \
                                Emisiones_CO2_mediano = ('Emisiones_CO2_mediano', 'median'), \
                                Emisiones_CO2_medio_sup = ('Emisiones_CO2_medio_sup', 'sum'), \
                                Emisiones_CO2_mediano_sup = ('Emisiones_CO2_mediano_sup', 'sum'), \
                                C_CCAA = ('C_CCAA', 'first'), \
                                CPROV = ('CPROV', 'first'), \
                                Numero_de_EPC = ('Numero_de_EPC', 'sum'), \
                                Numero_de_BI_certificados = ('Numero_de_BI_certificados', 'sum'), \
                                m2_certificados = ('m2_certificados', 'sum'), \
                                A_EP = ('A_EP', 'sum'), \
                                B_EP = ('B_EP', 'sum'), \
                                C_EP = ('C_EP', 'sum'), \
                                D_EP = ('D_EP', 'sum'), \
                                E_EP = ('E_EP', 'sum'), \
                                F_EP = ('F_EP', 'sum'), \
                                G_EP = ('G_EP', 'sum'), \
                                A_CO2 = ('A_CO2', 'sum'), \
                                B_CO2 = ('B_CO2', 'sum'), \
                                C_CO2 = ('C_CO2', 'sum'), \
                                D_CO2 = ('D_CO2', 'sum'), \
                                E_CO2 = ('E_CO2', 'sum'), \
                                F_CO2 = ('F_CO2', 'sum'), \
                                G_CO2 = ('G_CO2', 'sum'), \
                                A_EP_m2 = ('A_EP_m2', 'sum'), \
                                B_EP_m2 = ('B_EP_m2', 'sum'), \
                                C_EP_m2 = ('C_EP_m2', 'sum'), \
                                D_EP_m2 = ('D_EP_m2', 'sum'), \
                                E_EP_m2 = ('E_EP_m2', 'sum'), \
                                F_EP_m2 = ('F_EP_m2', 'sum'), \
                                G_EP_m2 = ('G_EP_m2', 'sum'), \
                                A_CO2_m2 = ('A_CO2_m2', 'sum'), \
                                B_CO2_m2 = ('B_CO2_m2', 'sum'), \
                                C_CO2_m2 = ('C_CO2_m2', 'sum'), \
                                D_CO2_m2 = ('D_CO2_m2', 'sum'), \
                                E_CO2_m2 = ('E_CO2_m2', 'sum'), \
                                F_CO2_m2 = ('F_CO2_m2', 'sum'), \
                                G_CO2_m2 = ('G_CO2_m2', 'sum'), \
                                A_EP_BI = ('A_EP_BI', 'sum'), \
                                B_EP_BI = ('B_EP_BI', 'sum'), \
                                C_EP_BI = ('C_EP_BI', 'sum'), \
                                D_EP_BI = ('D_EP_BI', 'sum'), \
                                E_EP_BI = ('E_EP_BI', 'sum'), \
                                F_EP_BI = ('F_EP_BI', 'sum'), \
                                G_EP_BI = ('G_EP_BI', 'sum'), \
                                A_CO2_BI = ('A_CO2_BI', 'sum'), \
                                B_CO2_BI = ('B_CO2_BI', 'sum'), \
                                C_CO2_BI = ('C_CO2_BI', 'sum'), \
                                D_CO2_BI = ('D_CO2_BI', 'sum'), \
                                E_CO2_BI = ('E_CO2_BI', 'sum'), \
                                F_CO2_BI = ('F_CO2_BI', 'sum'), \
                                G_CO2_BI = ('G_CO2_BI', 'sum'), \
                                )   
    print (df14_agrup.shape[0])

    df14_agrup.reset_index(drop = True, inplace = True)
    GranBBDD_resid.reset_index(drop = True, inplace = True)

    # Para sacar el nº de edificios residenciales certificados enteros
    num_df14_resid = df14_agrup.shape[0]

    # Al hacer esta unión elimino los EPC que tienen un certificado de edificio, luego las uniré con los EPC de edificios de nuevo que tendrán los Nº de BI y de m2 certificados bien, los del edificio
    print ('La BBDD total tenia y tiene: ')
    print (GranBBDD_resid.shape[0])

    concatenation = pd.DataFrame()
    concatenation = pd.concat([
                concatenation,
                GranBBDD_resid[GranBBDD_resid['ReferenciaCatastral_edificio'].isin(df14_agrup['ReferenciaCatastral_edificio']) == False],
                ])

    GranBBDD_resid = concatenation
    print (GranBBDD_resid.shape[0])

    GranBBDD_resid = pd.concat([GranBBDD_resid, df14_agrup], axis=0)
    print (GranBBDD_resid.shape[0])

    num_EPC_resid = GranBBDD_resid['Numero_de_EPC'].sum()

    # Para poder sacar el valor del consumo de energía y de emisiones ponderado por superficie, lo cmambio por el que estaba sin ponderar en este punto,
    # así si quiero hacer cualquier comprobación comparando valores puedo hacerlo solamente poniendo un _sup a las variables y quitando el drop y me salen ambos datos por edificio
    # El mediano ahora mismo no lo estoy sacando, no hago la mediana en ningún momento, lo dejo por si sirve para más adelante
    GranBBDD_resid.Consumo_energia_primaria_medio = GranBBDD_resid.Consumo_energia_primaria_medio_sup / GranBBDD_resid.m2_certificados
    # GranBBDD.Consumo_energia_primaria_mediano = GranBBDD.Consumo_energia_primaria_mediano_sup / GranBBDD.m2_certificados
    GranBBDD_resid.Emisiones_CO2_medio = GranBBDD_resid.Emisiones_CO2_medio_sup / GranBBDD_resid.m2_certificados
    # GranBBDD.Emisiones_CO2_mediano = GranBBDD.Emisiones_CO2_mediano_sup / GranBBDD.m2_certificados

    GranBBDD_resid = GranBBDD_resid.drop(['Consumo_energia_primaria_medio_sup'], axis=1)
    GranBBDD_resid = GranBBDD_resid.drop(['Consumo_energia_primaria_mediano_sup'], axis=1)
    GranBBDD_resid = GranBBDD_resid.drop(['Emisiones_CO2_medio_sup'], axis=1)
    GranBBDD_resid = GranBBDD_resid.drop(['Emisiones_CO2_mediano_sup'], axis=1)
    GranBBDD_resid = GranBBDD_resid.drop(['Consumo_energia_primaria_mediano'], axis=1)
    GranBBDD_resid = GranBBDD_resid.drop(['Emisiones_CO2_mediano'], axis=1)

    # Como Castilla La Mancha no da los datos de Consumo y emisiones, los resultados aquí salen 0 y para las medias nacionales cambiarian los resultados, hay que cambiarlos por None
    GranBBDD_resid.Consumo_energia_primaria_medio.replace ({0:None}, inplace=True)
    GranBBDD_resid.Emisiones_CO2_medio.replace ({0:None}, inplace=True)


    pre_borrar = GranBBDD_resid.shape[0]
    GranBBDD_resid['Coincide'] = np.where((GranBBDD_resid['m2_certificados']!= 0), 'Si','Bien')
    GranBBDD_resid = GranBBDD_resid.loc[(GranBBDD_resid['Coincide'] == 'Si')]
    GranBBDD_resid = GranBBDD_resid.drop(['Coincide'], axis=1)
    duplicados = GranBBDD_resid.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' edif resid')

    GranBBDD_resid.to_csv(b1_output + r"\Residencial_Todos_los_certificados_España_Pre_2024" + ".csv", index=False)
    GranBBDD_resid.to_parquet(b1_output + r"\Residencial_Todos_los_certificados_España_Pre_2024" + ".gzip", compression='gzip', index=False)

    # Datos no residenciales
    GranBBDD_terc = GranBBDD_terc.groupby('ReferenciaCatastral_edificio').agg(
                                ReferenciaCatastral_edificio = ('ReferenciaCatastral_edificio', 'first'), \
                                Consumo_energia_primaria_medio = ('Consumo_energia_primaria_medio', 'mean'), \
                                Consumo_energia_primaria_mediano = ('Consumo_energia_primaria_mediano', 'median'), \
                                Consumo_energia_primaria_medio_sup = ('Consumo_energia_primaria_medio_sup', 'sum'), \
                                Consumo_energia_primaria_mediano_sup = ('Consumo_energia_primaria_mediano_sup', 'sum'), \
                                Emisiones_CO2_medio = ('Emisiones_CO2_medio', 'mean'), \
                                Emisiones_CO2_mediano = ('Emisiones_CO2_mediano', 'median'), \
                                Emisiones_CO2_medio_sup = ('Emisiones_CO2_medio_sup', 'sum'), \
                                Emisiones_CO2_mediano_sup = ('Emisiones_CO2_mediano_sup', 'sum'), \
                                C_CCAA = ('C_CCAA', 'first'), \
                                CPROV = ('CPROV', 'first'), \
                                Numero_de_EPC = ('Numero_de_EPC', 'sum'), \
                                Numero_de_BI_certificados = ('Numero_de_BI_certificados', 'sum'), \
                                m2_certificados = ('m2_certificados', 'sum'), \
                                A_EP = ('A_EP', 'sum'), \
                                B_EP = ('B_EP', 'sum'), \
                                C_EP = ('C_EP', 'sum'), \
                                D_EP = ('D_EP', 'sum'), \
                                E_EP = ('E_EP', 'sum'), \
                                F_EP = ('F_EP', 'sum'), \
                                G_EP = ('G_EP', 'sum'), \
                                A_CO2 = ('A_CO2', 'sum'), \
                                B_CO2 = ('B_CO2', 'sum'), \
                                C_CO2 = ('C_CO2', 'sum'), \
                                D_CO2 = ('D_CO2', 'sum'), \
                                E_CO2 = ('E_CO2', 'sum'), \
                                F_CO2 = ('F_CO2', 'sum'), \
                                G_CO2 = ('G_CO2', 'sum'), \
                                A_EP_m2 = ('A_EP_m2', 'sum'), \
                                B_EP_m2 = ('B_EP_m2', 'sum'), \
                                C_EP_m2 = ('C_EP_m2', 'sum'), \
                                D_EP_m2 = ('D_EP_m2', 'sum'), \
                                E_EP_m2 = ('E_EP_m2', 'sum'), \
                                F_EP_m2 = ('F_EP_m2', 'sum'), \
                                G_EP_m2 = ('G_EP_m2', 'sum'), \
                                A_CO2_m2 = ('A_CO2_m2', 'sum'), \
                                B_CO2_m2 = ('B_CO2_m2', 'sum'), \
                                C_CO2_m2 = ('C_CO2_m2', 'sum'), \
                                D_CO2_m2 = ('D_CO2_m2', 'sum'), \
                                E_CO2_m2 = ('E_CO2_m2', 'sum'), \
                                F_CO2_m2 = ('F_CO2_m2', 'sum'), \
                                G_CO2_m2 = ('G_CO2_m2', 'sum'), \
                                A_EP_BI = ('A_EP_BI', 'sum'), \
                                B_EP_BI = ('B_EP_BI', 'sum'), \
                                C_EP_BI = ('C_EP_BI', 'sum'), \
                                D_EP_BI = ('D_EP_BI', 'sum'), \
                                E_EP_BI = ('E_EP_BI', 'sum'), \
                                F_EP_BI = ('F_EP_BI', 'sum'), \
                                G_EP_BI = ('G_EP_BI', 'sum'), \
                                A_CO2_BI = ('A_CO2_BI', 'sum'), \
                                B_CO2_BI = ('B_CO2_BI', 'sum'), \
                                C_CO2_BI = ('C_CO2_BI', 'sum'), \
                                D_CO2_BI = ('D_CO2_BI', 'sum'), \
                                E_CO2_BI = ('E_CO2_BI', 'sum'), \
                                F_CO2_BI = ('F_CO2_BI', 'sum'), \
                                G_CO2_BI = ('G_CO2_BI', 'sum'), \
                                )    
    h = GranBBDD_terc.shape[0]
    num_EPC_terc_prov = GranBBDD_terc['Numero_de_EPC'].sum()
    # Al hacer la unión de EPC por edificio, si había de edificio completo y de BI individual se han sumado el Nº de BI y los m2 certificados y hay más de que en edificio en si
    # Con este código le doy los valores de Nº de BI y los m2 certificados del EPC del edificio entero. Agrupo todos los EPC de edificio (para dejar las columnas y todo iguales, ya no debería haber EPC duplicados ni en la misma BBDD que se quita en el paso A1 ni que esté el mismo edificio en 2 BBDD diferentes que se quita en el A_8)
    print ('Datos para ver que esté bien: ')
    df14_terc = df14.loc[df14.loc[:, 'Uso_certificado'] == 'Terciario - Edificio completo']
    print (df14_terc.shape[0])
    df14_agrup = df14_terc.groupby('ReferenciaCatastral_edificio').agg(
                                ReferenciaCatastral_edificio = ('ReferenciaCatastral_edificio', 'first'), \
                                Consumo_energia_primaria_medio = ('Consumo_energia_primaria_medio', 'mean'), \
                                Consumo_energia_primaria_mediano = ('Consumo_energia_primaria_mediano', 'median'), \
                                Consumo_energia_primaria_medio_sup = ('Consumo_energia_primaria_medio_sup', 'sum'), \
                                Consumo_energia_primaria_mediano_sup = ('Consumo_energia_primaria_mediano_sup', 'sum'), \
                                Emisiones_CO2_medio = ('Emisiones_CO2_medio', 'mean'), \
                                Emisiones_CO2_mediano = ('Emisiones_CO2_mediano', 'median'), \
                                Emisiones_CO2_medio_sup = ('Emisiones_CO2_medio_sup', 'sum'), \
                                Emisiones_CO2_mediano_sup = ('Emisiones_CO2_mediano_sup', 'sum'), \
                                C_CCAA = ('C_CCAA', 'first'), \
                                CPROV = ('CPROV', 'first'), \
                                Numero_de_EPC = ('Numero_de_EPC', 'sum'), \
                                Numero_de_BI_certificados = ('Numero_de_BI_certificados', 'sum'), \
                                m2_certificados = ('m2_certificados', 'sum'), \
                                A_EP = ('A_EP', 'sum'), \
                                B_EP = ('B_EP', 'sum'), \
                                C_EP = ('C_EP', 'sum'), \
                                D_EP = ('D_EP', 'sum'), \
                                E_EP = ('E_EP', 'sum'), \
                                F_EP = ('F_EP', 'sum'), \
                                G_EP = ('G_EP', 'sum'), \
                                A_CO2 = ('A_CO2', 'sum'), \
                                B_CO2 = ('B_CO2', 'sum'), \
                                C_CO2 = ('C_CO2', 'sum'), \
                                D_CO2 = ('D_CO2', 'sum'), \
                                E_CO2 = ('E_CO2', 'sum'), \
                                F_CO2 = ('F_CO2', 'sum'), \
                                G_CO2 = ('G_CO2', 'sum'), \
                                A_EP_m2 = ('A_EP_m2', 'sum'), \
                                B_EP_m2 = ('B_EP_m2', 'sum'), \
                                C_EP_m2 = ('C_EP_m2', 'sum'), \
                                D_EP_m2 = ('D_EP_m2', 'sum'), \
                                E_EP_m2 = ('E_EP_m2', 'sum'), \
                                F_EP_m2 = ('F_EP_m2', 'sum'), \
                                G_EP_m2 = ('G_EP_m2', 'sum'), \
                                A_CO2_m2 = ('A_CO2_m2', 'sum'), \
                                B_CO2_m2 = ('B_CO2_m2', 'sum'), \
                                C_CO2_m2 = ('C_CO2_m2', 'sum'), \
                                D_CO2_m2 = ('D_CO2_m2', 'sum'), \
                                E_CO2_m2 = ('E_CO2_m2', 'sum'), \
                                F_CO2_m2 = ('F_CO2_m2', 'sum'), \
                                G_CO2_m2 = ('G_CO2_m2', 'sum'), \
                                A_EP_BI = ('A_EP_BI', 'sum'), \
                                B_EP_BI = ('B_EP_BI', 'sum'), \
                                C_EP_BI = ('C_EP_BI', 'sum'), \
                                D_EP_BI = ('D_EP_BI', 'sum'), \
                                E_EP_BI = ('E_EP_BI', 'sum'), \
                                F_EP_BI = ('F_EP_BI', 'sum'), \
                                G_EP_BI = ('G_EP_BI', 'sum'), \
                                A_CO2_BI = ('A_CO2_BI', 'sum'), \
                                B_CO2_BI = ('B_CO2_BI', 'sum'), \
                                C_CO2_BI = ('C_CO2_BI', 'sum'), \
                                D_CO2_BI = ('D_CO2_BI', 'sum'), \
                                E_CO2_BI = ('E_CO2_BI', 'sum'), \
                                F_CO2_BI = ('F_CO2_BI', 'sum'), \
                                G_CO2_BI = ('G_CO2_BI', 'sum'), \
                                )   
    print (df14_agrup.shape[0])

    df14_agrup.reset_index(drop = True, inplace = True)
    GranBBDD_terc.reset_index(drop = True, inplace = True)

    num_df14_terc = df14_agrup.shape[0]

    # Al hacer esta unión elimino los EPC que tienen un certificado de edificio, luego las uniré con los EPC de edificios de nuevo que tendrán los Nº de BI y de m2 certificados bien, los del edificio
    print ('La BBDD total tenia y tiene: ')
    print (GranBBDD_terc.shape[0])

    concatenation = pd.DataFrame()
    concatenation = pd.concat([
                concatenation,
                GranBBDD_terc[GranBBDD_terc['ReferenciaCatastral_edificio'].isin(df14_agrup['ReferenciaCatastral_edificio']) == False],
                ])

    GranBBDD_terc = concatenation
    print (GranBBDD_terc.shape[0])

    GranBBDD_terc = pd.concat([GranBBDD_terc, df14_agrup], axis=0)
    print (GranBBDD_terc.shape[0])

    num_EPC_terc = GranBBDD_terc['Numero_de_EPC'].sum()

    # Para poder sacar el valor del consumo de energía y de emisiones ponderado por superficie, lo cmambio por el que estaba sin ponderar en este punto,
    # así si quiero hacer cualquier comprobación comparando valores puedo hacerlo solamente poniendo un _sup a las variables y quitando el drop y me salen ambos datos por edificio
    # El mediano ahora mismo no lo estoy sacando, no hago la mediana en ningún momento, lo dejo por si sirve para más adelante
    GranBBDD_terc.Consumo_energia_primaria_medio = GranBBDD_terc.Consumo_energia_primaria_medio_sup / GranBBDD_terc.m2_certificados
    # GranBBDD.Consumo_energia_primaria_mediano = GranBBDD.Consumo_energia_primaria_mediano_sup / GranBBDD.m2_certificados
    GranBBDD_terc.Emisiones_CO2_medio = GranBBDD_terc.Emisiones_CO2_medio_sup / GranBBDD_terc.m2_certificados
    # GranBBDD.Emisiones_CO2_mediano = GranBBDD.Emisiones_CO2_mediano_sup / GranBBDD.m2_certificados

    GranBBDD_terc = GranBBDD_terc.drop(['Consumo_energia_primaria_medio_sup'], axis=1)
    GranBBDD_terc = GranBBDD_terc.drop(['Consumo_energia_primaria_mediano_sup'], axis=1)
    GranBBDD_terc = GranBBDD_terc.drop(['Emisiones_CO2_medio_sup'], axis=1)
    GranBBDD_terc = GranBBDD_terc.drop(['Emisiones_CO2_mediano_sup'], axis=1)
    GranBBDD_terc = GranBBDD_terc.drop(['Consumo_energia_primaria_mediano'], axis=1)
    GranBBDD_terc = GranBBDD_terc.drop(['Emisiones_CO2_mediano'], axis=1)

    # Como Castilla La Mancha no da los datos de Consumo y emisiones, los resultados aquí salen 0 y para las medias nacionales cambiarian los resultados, hay que cambiarlos por None
    GranBBDD_terc.Consumo_energia_primaria_medio.replace ({0:None}, inplace=True)
    GranBBDD_terc.Emisiones_CO2_medio.replace ({0:None}, inplace=True)

    pre_borrar = GranBBDD_terc.shape[0]
    GranBBDD_terc['Coincide'] = np.where((GranBBDD_terc['m2_certificados']!= 0), 'Si','Bien')
    GranBBDD_terc = GranBBDD_terc.loc[(GranBBDD_terc['Coincide'] == 'Si')]
    GranBBDD_terc = GranBBDD_terc.drop(['Coincide'], axis=1)
    duplicados = GranBBDD_terc.shape[0] - pre_borrar
    if duplicados != 0:
        print ('Se han borrado por 0m2 ' + str(duplicados) + ' edif no resid')

    GranBBDD_terc.to_csv(b1_output + r"\Terciario_Todos_los_certificados_España_Pre_2024" + ".csv", index=False)
    GranBBDD_terc.to_parquet(b1_output + r"\Terciario_Todos_los_certificados_España_Pre_2024" + ".gzip", compression='gzip', index=False)

    print('Del total de EPC: ' + str(c) + ' hay ' + str(d) + ' con uso residencial y ' + str(e) + ' con uso no residencial \n'
        + 'Hay un total de ' + str(w) + ' edificios certificados \n'
        + 'Hay un total de ' + str(g) + ' edificios certificados con datos residenciales \n'      
        + 'Hay un total de ' + str(h) + ' edificios certificados con datos terciarios  \n'
        + 'Entre medio quedan ' + str(num_EPC_todos_prov) + ' EPC con uso todos  \n'
        + 'Entre medio quedan ' + str(num_EPC_resid_prov) + ' EPC con uso resid  \n'
        + 'Entre medio quedan ' + str(num_EPC_terc_prov) + ' EPC con uso terc  \n'
        + 'Al final quedan ' + str(num_EPC_todos) + ' EPC con uso todos  \n'
        + 'Al final quedan ' + str(num_EPC_resid) + ' EPC con uso resid  \n'
        + 'Al final quedan ' + str(num_EPC_terc) + ' EPC con uso terc  \n'
        + 'Hay ' + str(num_df14_resid) + ' edificios residenciales certificados enteros en el modelo  \n'
        + 'Hay ' + str(num_df14_terc) + ' edificios no residenciales certificados enteros en el modelo  \n'
        )



    with open(b1_output + r'\BBDD_EPC_Unidas_por_edificio_datos_alfanum' + ".txt", 'w') as f:
            f.write('Del total de EPC: ' + str(c) + ' hay ' + str(d) + ' con uso residencial y ' + str(e) + ' con uso no residencial \n'
        + 'Hay un total de ' + str(w) + ' edificios certificados \n'
        + 'Hay un total de ' + str(g) + ' edificios certificados con datos residenciales \n'      
        + 'Hay un total de ' + str(h) + ' edificios certificados con datos terciarios  \n'
        + 'Entre medio quedan ' + str(num_EPC_todos_prov) + ' EPC con uso todos  \n'
        + 'Entre medio quedan ' + str(num_EPC_resid_prov) + ' EPC con uso resid  \n'
        + 'Entre medio quedan ' + str(num_EPC_terc_prov) + ' EPC con uso terc  \n'
        + 'Al final quedan ' + str(num_EPC_todos) + ' EPC con uso todos  \n'
        + 'Al final quedan ' + str(num_EPC_resid) + ' EPC con uso resid  \n'
        + 'Al final quedan ' + str(num_EPC_terc) + ' EPC con uso terc  \n'
        + 'Hay ' + str(num_df14_resid) + ' edificios residenciales certificados enteros en el modelo  \n'
        + 'Hay ' + str(num_df14_terc) + ' edificios no residenciales certificados enteros en el modelo  \n'
        )

    duracion_A = time() - inicio
    print('En total ha tardado: ' + str(duracion_A) + ' segundos')

    print ('Terminado')



